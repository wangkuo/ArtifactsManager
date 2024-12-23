import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request

# 加载 .env 文件
load_dotenv()

app = Flask(__name__)

# 配置 GitHub API 访问凭证
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USER = os.getenv('GITHUB_USER')

@app.route('/artifacts')
def artifacts():
    # 获取仓库列表
    repos_url = f'https://api.github.com/users/{GITHUB_USER}/repos'
    repos_response = requests.get(repos_url, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    repos = repos_response.json()

    # 存储 Artifacts 信息的列表
    artifacts_info = []

    # 遍历仓库，获取每个仓库的 Artifacts
    for repo in repos:
        repo_name = repo['name']
        artifacts_url = f'https://api.github.com/repos/{GITHUB_USER}/{repo_name}/actions/artifacts'
        artifacts_response = requests.get(artifacts_url, headers={'Authorization': f'token {GITHUB_TOKEN}'})
        artifacts = artifacts_response.json()

        # 将 Artifacts 信息添加到列表中
        for artifact in artifacts['artifacts']:
            artifacts_info.append({
                'repo_name': repo_name,
                'artifact_name': artifact['name'],
                'created_at': artifact['created_at'],
                'expired': artifact['expired'],
                'id': artifact['id']
            })

    # 渲染模板并传递 Artifacts 信息
    return render_template('artifacts.html', artifacts=artifacts_info)

@app.route('/delete_artifact', methods=['POST'])
def delete_artifact():
    # 从请求中获取 artifact_id 和 repo_name
    artifact_id = request.form.get('artifact_id')
    repo_name = request.form.get('repo_name')

    # 构建删除 Artifact 的 URL
    delete_url = f'https://api.github.com/repos/{GITHUB_USER}/{repo_name}/actions/artifacts/{artifact_id}'

    # 发送 DELETE 请求到 GitHub API
    response = requests.delete(delete_url, headers={'Authorization': f'token {GITHUB_TOKEN}'})

    # 根据响应判断删除是否成功
    if response.status_code == 204:
        return 'Artifact deleted successfully'
    else:
        return 'Failed to delete artifact'

if __name__ == '__main__':
    app.run()
