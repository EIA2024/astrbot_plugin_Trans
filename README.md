# Trans翻译器 (Trans Translator)

AstrBot 哦齁语翻译器插件 - 将文本与哦齁语之间进行转换

本项目基于 [https://msbt.seku.su/](https://msbt.seku.su/) 的编码解码功能，受 [@koishijs/koishi-plugin-msbt](https://github.com/koishijs/koishi-plugin-msbt.git) 启发开发。

## 功能特性

- 🔄 **文本编码**: 将普通文本编码为哦齁语
- 🔍 **文本解码**: 将哦齁语文本解码为普通文本  
- 📖 **帮助系统**: 内置使用帮助和示例
- 🛡️ **错误处理**: 完善的错误提示和异常处理

## 使用方法

### 编码功能
```
/encode <文本>
```
将普通文本编码为哦齁语

### 解码功能
```
/decode <哦齁语文本>
```
将哦齁语文本解码为普通文本

### 帮助信息
```
/Trans_help
```
显示详细的使用帮助和示例

## 示例

**编码示例:**
```
/encode Hello, world!
```
输出: `咕～嗯咿嗯哼嗯哼嗯呼噢哼噢齁啊啊嗯呼啊噢嗯哼嗯咕噢哦`

**解码示例:**
```
/decode 咕～嗯咿嗯哼嗯哼嗯呼噢哼噢齁啊啊嗯呼啊噢嗯哼嗯咕噢哦
```
输出: `Hello, world!`

## 安装

1. 确保已安装 AstrBot
2. 安装依赖: `pip install -r requirements.txt`
3. 将插件文件放入 AstrBot 插件目录
4. 重启 AstrBot 或重新加载插件

## 依赖

- astrbot>=1.0.0

## 支持

[帮助文档](https://astrbot.app)

## 致谢

- 基于 [https://msbt.seku.su/](https://msbt.seku.su/) 的编码解码功能
- 受 [@koishijs/koishi-plugin-msbt](https://github.com/koishijs/koishi-plugin-msbt.git) 启发开发

## 许可证

本项目基于原 helloworld 的功能开发，遵循相应的开源许可证。
