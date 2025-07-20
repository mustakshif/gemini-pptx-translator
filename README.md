# PPTX Translate with Gemini API (Fixed Version)

基于Google Gemini API的PowerPoint演示文稿翻译工具，支持多种Gemini模型选择，具备改进的文本提取算法和智能进度跟踪。

## 功能特点

- 使用Google Gemini API进行高质量翻译
- **改进的文本提取算法** - 按段落完整提取文本，避免格式破坏
- **智能进度跟踪系统** - 实时显示翻译进度、ETA时间估算和进度条
- 支持多种最新Gemini模型选择（包括Gemini 2.5系列）
- 提取PowerPoint中的文本内容（包括标题、正文、表格单元格）
- **异步批量翻译** - 高效处理大量文本内容
- **智能缓存机制** - 避免重复API调用，支持断点续传
- **增强的错误处理** - 超时控制、配额检测、自动重试
- **格式保持算法** - 保持原始文本格式和样式
- 详细的日志记录和多种输出模式
- 命令行界面，支持单文件或批量处理

## 核心算法改进

### 1. 文本提取算法优化
- **段落级提取**：按完整段落提取文本，而不是按文本片段分割
- **表格处理增强**：完整提取表格单元格内容，保持数据完整性
- **格式保持**：在翻译过程中保留原始格式和样式

### 2. 智能进度跟踪
- **实时进度条**：显示可视化进度条和百分比
- **ETA计算**：基于当前速度估算剩余时间
- **内存优化**：高效处理大文件的进度显示

### 3. 异步翻译引擎
- **批量处理**：同时处理多个文本元素
- **超时控制**：30秒API调用超时，防止卡死
- **错误恢复**：API失败时保留原始文本，继续处理

## 支持的Gemini模型

### 最新版本 (Gemini 2.5) 🆕
- `gemini-2.5-flash`: 最新Gemini 2.5 Flash模型（最快最高效，**默认推荐**）
- `gemini-2.5-pro`: 最新Gemini 2.5 Pro模型（最强大，适合复杂翻译任务）

### 实验版本 (Gemini 2.0)
- `gemini-2.0-flash-exp`: 实验版Flash模型
- `gemini-2.0-flash`: 稳定版Flash模型  
- `gemini-2.0-pro`: Pro模型

### 历史版本 (Gemini 1.5)
- `gemini-1.5-flash`: 历史Flash模型
- `gemini-1.5-pro`: 历史Pro模型
- `gemini-1.5-flash-exp`: 历史实验版Flash
- `gemini-1.5-pro-exp`: 历史实验版Pro

## 安装

1. 克隆或下载项目文件
2. 安装依赖包：
```bash
pip install -r requirements.txt
```

## 获取Gemini API密钥

1. 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 创建新的API密钥
3. 将API密钥设置为环境变量：

```bash
export GEMINI_API_KEY="YOUR GEMINI API KEY HERE"
```

## 使用方法

### 基本用法

翻译单个文件（使用默认的gemini-2.5-flash模型）：
```bash
python translator.py presentation.pptx -l en
```

指定输出文件：
```bash
python translator.py presentation.pptx -l zh-CN -o translated.pptx
```

使用Pro模型进行高质量翻译：
```bash
python translator.py presentation.pptx -l es -m gemini-2.5-pro
```

### 批量处理

翻译当前目录下所有PPT文件：
```bash
python translator.py -l fr
```

### 查看可用模型

```bash
python translator.py --list-models
```

### 验证模型可用性

```bash
# 完整验证（可能较慢）
python verify_models.py

# 快速验证（推荐）
python quick_test.py

# 基本诊断
python diagnose.py
```

### 命令行参数详解

- `input_file`: 输入的PowerPoint文件（.pptx）
- `-l, --language`: 目标语言代码（必需）
- `-o, --output`: 输出文件路径
- `-k, --api_key`: Gemini API密钥（或设置GEMINI_API_KEY环境变量）
- `-m, --model`: 使用的Gemini模型（默认：gemini-2.5-flash）
- `--list-models`: 列出可用模型并退出
- `--profile`: 启用性能分析和处理时间统计
- `--verbose`: 显示详细翻译进度（逐条文本显示）
- `--quiet`: 最小化输出（仅显示错误和最终结果）

### 支持的语言代码

- `en`: 英语
- `zh-CN`: 简体中文
- `zh-TW`: 繁体中文
- `es`: 西班牙语
- `fr`: 法语
- `de`: 德语
- `ja`: 日语
- `ko`: 韩语
- `ar`: 阿拉伯语
- `ru`: 俄语
- `pt`: 葡萄牙语
- `it`: 意大利语
- `nl`: 荷兰语
- `sv`: 瑞典语
- 等等...

## 使用示例

### 中文翻译为英文（显示进度条）
```bash
python translator.py 外交思想和务实行动.pptx -l en
# 输出: Translating to en: ████████████████████████████████████████████████████ 100.0% (45/45) Completed in 23.4s
```

### 英文翻译为中文（详细模式）
```bash
python translator.py presentation.pptx -l zh-CN -o 翻译后的演示文稿.pptx --verbose
```

### 使用最新Pro模型进行高质量翻译
```bash
python translator.py presentation.pptx -l es -m gemini-2.5-pro
```

### 性能分析模式
```bash
python translator.py presentation.pptx -l en --profile
# 显示详细的处理时间统计
```

### 静默模式（仅显示结果）
```bash
python translator.py presentation.pptx -l en --quiet
```

## 智能缓存系统

脚本会自动创建翻译缓存文件，实现以下功能：
- **避免重复翻译**：相同文本不会重复调用API
- **断点续传**：翻译中断后可以继续之前的进度
- **文件特定缓存**：每个文件和语言组合有独立的缓存

缓存文件格式：
```
translation_cache_{文件名}_{语言}_{哈希值}.json
```

## 日志系统

翻译过程会记录到：
- **控制台输出**：实时进度和状态信息
- **日志文件**：`translation_log.txt` - 详细的操作记录
- **进度跟踪**：可视化进度条和ETA时间估算

## 性能特点

### 处理速度
- **异步处理**：并发处理多个文本元素
- **智能缓存**：避免重复API调用
- **批量优化**：减少API请求次数

### 错误处理
- **30秒超时控制**：防止API调用卡死
- **配额检测**：自动识别API配额问题
- **优雅降级**：API失败时保留原始文本

### 内存优化
- **流式处理**：逐步处理大文件
- **缓存管理**：自动保存和加载翻译缓存

## 注意事项

1. **API配额管理**：确保有足够的Gemini API配额
2. **文件大小**：大文件翻译可能需要较长时间，建议使用进度条模式
3. **备份建议**：建议在翻译前备份原始文件
4. **格式兼容**：某些特殊PowerPoint格式可能无法完全保留
5. **网络稳定性**：确保网络连接稳定，避免API超时

## 故障排除

### 常见问题

1. **API密钥错误**
   - 检查GEMINI_API_KEY环境变量是否正确设置
   - 或使用 `-k` 参数直接提供API密钥
   - 运行 `python diagnose.py` 进行基本诊断

2. **模型不可用**
   - 使用 `--list-models` 查看可用模型
   - 运行 `python quick_test.py` 快速验证
   - 推荐使用默认的 `gemini-2.5-flash` 模型

3. **翻译进度卡住**
   - 脚本已加入30秒超时控制
   - 检查网络连接稳定性
   - 尝试使用 `--verbose` 模式查看详细进度

4. **文件读取错误**
   - 确保文件路径正确且文件未被占用
   - 检查文件是否为有效的PowerPoint格式（.pptx）
   - 确认文件权限允许读取

5. **翻译质量问题**
   - 尝试使用 `gemini-2.5-pro` 模型获得更好的翻译质量
   - 检查原始文本是否清晰完整
   - 使用 `--verbose` 模式检查具体翻译内容

6. **API超时或配额问题**
   - 检查Gemini API配额使用情况
   - 脚本已添加智能重试机制
   - 大文件可考虑分批处理或使用缓存续传

### 性能优化建议

1. **选择合适的模型**：
   - 日常使用：`gemini-2.5-flash`（速度快）
   - 高质量翻译：`gemini-2.5-pro`（质量高）

2. **利用缓存机制**：
   - 保留缓存文件以支持断点续传
   - 相同内容不会重复翻译

3. **批量处理**：
   - 使用目录批量翻译提高效率
   - 利用 `--quiet` 模式减少输出开销

## 许可证

本项目基于MIT许可证开源。

## 贡献

欢迎提交Issue和Pull Request来改进这个工具。特别欢迎以下方面的贡献：
- 新的文本提取算法优化
- 更多语言支持
- 性能改进建议
- 错误处理增强

---

*本仓库文件由 [Cursor](https://cursor.sh/) AI 编程助手生成* 