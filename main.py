from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger


class TransEncoder:
    """哦齁语编码解码器"""
    
    def __init__(self):
        # 编码表，包含16个特殊字符
        self.codebook = ['齁', '哦', '噢', '喔', '咕', '咿', '嗯', '啊', '～', '哈', '！', '唔', '哼', '❤', '呃', '呼']
        # 创建反向映射字典
        self.codebook_map = {char: i for i, char in enumerate(self.codebook)}
    
    def encode(self, input_text: str) -> str:
        """
        将文本编码为哦齁语
        
        Args:
            input_text: 要编码的文本
            
        Returns:
            编码后的哦齁语字符串
        """
        # 将文本转换为UTF-8字节
        bytes_data = input_text.encode('utf-8')
        encoded = ''
        
        for byte in bytes_data:
            # 提取高4位和低4位
            high = (byte >> 4) & 0x0F
            low = byte & 0x0F
            # 根据编码表转换为哦齁语字符
            encoded += self.codebook[high] + self.codebook[low]
        
        return encoded
    
    def decode(self, input_text: str) -> str:
        """
        将哦齁语文本解码为原始文本
        
        Args:
            input_text: 要解码的哦齁语文本
            
        Returns:
            解码后的原始文本，如果失败则返回错误信息
        """
        # 检查输入长度是否为偶数
        if len(input_text) % 2 != 0:
            return "错误：输入长度必须为偶数"
        
        bytes_list = []
        
        # 每两个字符为一组进行解码
        for i in range(0, len(input_text), 2):
            high_char = input_text[i]
            low_char = input_text[i + 1]
            
            # 查找字符对应的数值
            high = self.codebook_map.get(high_char)
            low = self.codebook_map.get(low_char)
            
            # 检查是否包含非法字符
            if high is None or low is None:
                return "错误：输入包含非法字符"
            
            # 重新组合字节
            byte = (high << 4) | low
            bytes_list.append(byte)
        
        try:
            # 尝试解码为UTF-8文本
            decoded = bytes(bytes_list).decode('utf-8')
            return decoded
        except UnicodeDecodeError:
            # 如果无法解码为UTF-8，返回十六进制表示
            hex_bytes = ' '.join(f'{b:02x}' for b in bytes_list)
            return f"错误：无法正确解码为UTF-8文本\n十六进制表示: {hex_bytes}"


@register("trans_translator", "YourName", "哦齁语翻译器 - 将文本与哦齁语之间进行转换", "1.0.0")
class TransTranslatorPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.encoder = TransEncoder()

    async def initialize(self):
        """插件初始化方法"""
        logger.info("哦齁语翻译器插件已初始化")
    
    @filter.command("encode")
    async def encode_text(self, event: AstrMessageEvent):
        """将文本编码为哦齁语"""
        # 获取完整的消息字符串
        full_message = event.message_str.strip()
        
        # 移除命令前缀，支持多种格式
        text_to_encode = full_message
        
        # 移除 /encode 前缀
        if text_to_encode.startswith('/encode'):
            text_to_encode = text_to_encode[7:].strip()
        # 移除 encode 前缀（不带斜杠）
        elif text_to_encode.startswith('encode '):
            text_to_encode = text_to_encode[7:].strip()
        
        # 调试信息
        logger.info(f"完整消息: '{full_message}'")
        logger.info(f"提取的文本: '{text_to_encode}'")
        
        if not text_to_encode:
            yield event.plain_result("请提供要编码的文本！\n使用方法：/encode <文本>")
            return
        
        try:
            encoded_result = self.encoder.encode(text_to_encode)
            yield event.plain_result(f"编码结果：\n{encoded_result}")
        except Exception as e:
            logger.error(f"编码过程中发生错误：{e}")
            yield event.plain_result(f"编码失败：{str(e)}")

    @filter.command("decode")
    async def decode_text(self, event: AstrMessageEvent):
        """将哦齁语文本解码为原始文本"""
        # 获取完整的消息字符串
        full_message = event.message_str.strip()
        
        # 移除命令前缀，支持多种格式
        text_to_decode = full_message
        
        # 移除 /decode 前缀
        if text_to_decode.startswith('/decode'):
            text_to_decode = text_to_decode[7:].strip()
        # 移除 decode 前缀（不带斜杠）
        elif text_to_decode.startswith('decode '):
            text_to_decode = text_to_decode[7:].strip()
        
        # 调试信息
        logger.info(f"完整消息: '{full_message}'")
        logger.info(f"提取的文本: '{text_to_decode}'")
        
        if not text_to_decode:
            yield event.plain_result("请提供要解码的哦齁语文本！\n使用方法：/decode <哦齁语文本>")
            return
        
        try:
            decoded_result = self.encoder.decode(text_to_decode)
            if decoded_result.startswith("错误："):
                yield event.plain_result(f"解码失败：{decoded_result}")
            else:
                yield event.plain_result(f"解码结果：\n{decoded_result}")
        except Exception as e:
            logger.error(f"解码过程中发生错误：{e}")
            yield event.plain_result(f"解码失败：{str(e)}")

    @filter.command("Trans_help")
    async def show_help(self, event: AstrMessageEvent):
        """显示哦齁语翻译器的使用帮助"""
        help_text = """哦齁语翻译器使用帮助：

📝 编码功能：
/encode <文本> - 将普通文本编码为哦齁语

🔍 解码功能：
/decode <哦齁语文本> - 将哦齁语文本解码为普通文本

💡 示例：
/encode Hello, world!
/decode 咕～嗯咿嗯哼嗯哼嗯呼噢哼噢齁啊啊嗯呼啊噢嗯哼嗯咕噢哦

❓ 帮助：
/Trans_help - 显示此帮助信息

基于 https://msbt.seku.su/ 的编码解码功能"""
        
        yield event.plain_result(help_text)

    async def terminate(self):
        """插件销毁方法"""
        logger.info("哦齁语翻译器插件已卸载")
