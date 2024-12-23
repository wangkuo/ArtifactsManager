# GitHub Artifacts Manager

GitHub Artifacts Manager 是一个用于管理 GitHub Actions 构建产物（Artifacts）的 Web 应用。它提供了一个简单的界面来查看和删除您的 GitHub 仓库中的所有 Artifacts。

## 功能特点

- 显示所有仓库的 Artifacts 列表
- 查看 Artifacts 的详细信息（仓库名、创建时间、是否过期等）
- 一键删除不需要的 Artifacts
- 自动刷新数据显示

## 技术栈

- Backend: Python Flask
- Frontend: HTML, JavaScript
- API: GitHub REST API
- 依赖管理: pip

## 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/your-username/artifacts-manager.git
cd artifacts-manager
```
2. 创建并激活虚拟环境：
```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```
3. 安装依赖：
```bash
pip install -r requirements.txt
```
4. 配置环境变量：
创建 `.env` 文件并添加以下配置：
```
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_USER=your_github_username
```
注意：您需要创建一个具有 `repo` 和 `workflow` 权限的 GitHub Personal Access Token。

## 使用方法

1. 启动应用：
```bash
python app.py
```

2. 在浏览器中访问：`http://localhost:5000/artifacts`

3. 功能说明：
   - 查看 Artifacts：页面会显示所有仓库的 Artifacts 列表
   - 删除 Artifacts：点击每个 Artifact 右侧的"删除"按钮
   - 确认删除：系统会提示确认，确认后即可删除

## API 说明

### 获取 Artifacts 列表
- 路由：`/artifacts`
- 方法：GET
- 返回：包含所有 Artifacts 信息的 HTML 页面

### 删除 Artifact
- 路由：`/delete_artifact`
- 方法：POST
- 参数：
  - `artifact_id`: Artifact 的 ID
  - `repo_name`: 仓库名称
- 返回：
  - 成功：`Artifact deleted successfully`
  - 失败：`Failed to delete artifact`

## 注意事项

1. 请确保您的 GitHub Token 具有足够的权限
2. 删除操作不可恢复，请谨慎操作
3. 建议定期清理不需要的 Artifacts 以节省存储空间


## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 联系方式

如有问题或建议，请提交 Issue 或联系项目维护者。

