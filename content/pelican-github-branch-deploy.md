Title: Pelican+GitHub.io博客进阶：分支管理、自动化部署与版本控制全解析
Date: 2025-12-24 14:21
Modified: 2025-12-24 14:21
Category: 技术,教程
Tags: pelican,github.io,分支管理,自动化部署,版本控制
Slug: pelican-github-branch-deploy
Author: 田冲憨娃

### 前言
上一篇博客分享了用Pelican+GitHub.io搭建个人博客的基础流程，成功部署了第一篇文章到unclevicky.github.io。但随着操作深入，不少朋友（包括我自己）会发现仓库里多了几个分支——main、gh-pages、master，还在main分支下看到了`.github/workflow/pelican.yml`文件。

这些分支分别是干什么的？yml文件是用来实现什么功能的？博客的源文件（写的文章、配置文件）和发布后的静态文件该怎么分开管理？这篇进阶教程就来一一拆解这些疑问，帮大家理清GitHub仓库的结构逻辑，掌握规范的版本管理方法，让后续写博客、维护博客更高效～

## 一、先搞懂：仓库里的三个分支到底各司其职？
在unclevicky.github.io仓库中出现的main、gh-pages、master三个分支，并非多余，而是GitHub Pages部署和Pelican工作流的核心组成部分，每个分支都有明确的分工：

### 1. main分支：你的「博客源文件大本营」
**核心作用**：存储博客的所有源文件，是你日常编辑、维护的主要分支。
里面包含的内容（也是上一篇教程中搭建的blog目录文件）：
```
blog/  
├── content/ # 你写的所有markdown文章（.md文件）
├── pelicanconf.py # 博客主配置文件（主题、插件、站点信息等）
├── publishconf.py # 发布配置文件
├── Makefile # 自动化脚本（可选）
├── .github/workflow/pelican.yml # 自动化部署配置文件
└── 其他：插件目录、静态资源目录（images/photos）等
```
**操作逻辑**：日常写文章、修改配置、安装插件，都在这个分支下操作，写完后用git提交更新，相当于给源文件做版本备份。

### 2. gh-pages分支：「博客发布的静态文件仓库」
**核心作用**：存储Pelican生成的静态网站文件，是GitHub Pages实际部署、对外访问的分支。
里面的内容对应Pelican生成的`output`目录：
```
output/  
├── index.html # 博客首页
├── 2020/04/ # 按日期分类的文章页面
├── static/ # 静态资源（图片、CSS、JS）
└── 其他HTML页面、站点地图等
```
**操作逻辑**：这个分支不需要手动修改！所有文件都是通过自动化工具（后面讲的pelican.yml）从main分支的源文件生成的，GitHub Pages会自动读取这个分支的内容，展示成大家访问到的`https://unclevicky.github.io`。

### 3. master分支：「历史遗留的「退休」分支」
**核心作用**：早期GitHub Pages的默认部署分支（以前GitHub Pages优先读取master分支的根目录文件），现在大多被gh-pages或main分支替代。
**现状说明**：如果你的仓库是早期创建的，或者之前手动部署过，可能会保留这个分支。目前它的作用和gh-pages重复，属于「退休状态」，一般不需要再维护。

### 三个分支对比表
| 分支名称 | 核心用途 | 操作方式 | 关键文件/目录 |
|----------|----------|----------|---------------|
| main     | 存储源文件（编辑、维护） | 日常编辑、git提交更新 | content/、pelicanconf.py、pelican.yml |
| gh-pages | 存储发布文件（部署、访问） | 自动化生成，无需手动改 | index.html、static/、按日期分类的文章目录 |
| master   | 历史部署分支（兼容旧版） | 无需维护，可清理 | 早期手动上传的output文件（已过时） |

### 可视化理解（用pelican-photos插件展示分支逻辑）
<div gallery="{photo}branch-deploy"></div>

## 二、关键文件解析：pelican.yml是自动化部署的「幕后推手」
在main分支的`.github/workflow/`目录下的`pelican.yml`文件，是实现「提交源文件→自动生成→自动发布」的核心，本质是GitHub Actions的工作流配置文件。

### 1. GitHub Actions是什么？
简单说，GitHub Actions是GitHub内置的自动化工具，可以让你在仓库发生特定事件（比如提交代码、创建分支）时，自动执行一系列命令（比如安装依赖、运行脚本、部署文件）。而pelican.yml就是告诉GitHub Actions：当我向main分支提交代码时，要做哪些步骤来部署博客。

### 2. pelican.yml的核心配置（以常见模板为例）
```yaml
name: Pelican Build and Deploy # 工作流名称
on:
  push:
    branches: [ main ] # 触发条件：向main分支推送代码时执行
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest # 运行环境：Ubuntu系统
    steps:
      - name: Checkout main branch # 步骤1：拉取main分支的源文件
        uses: actions/checkout@v4
      - name: Set up Python # 步骤2：安装Python环境（Pelican基于Python）
        uses: actions/setup-python@v5
        with:
          python-version: '3.10' # 指定Python版本
      - name: Install dependencies # 步骤3：安装Pelican及依赖包
        run: |
          python -m pip install --upgrade pip
          pip install pelican markdown pelican-photos # 安装所需包
      - name: Build Pelican site # 步骤4：生成静态网站文件
        run: pelican content -s publishconf.py # 执行pelican命令，生成output目录
      - name: Deploy to gh-pages # 步骤5：将output文件推送到gh-pages分支
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }} # GitHub自动生成的令牌（无需手动配置）
          publish_dir: ./output # 要部署的目录（即Pelican生成的output）
          publish_branch: gh-pages # 部署到的分支
```

### 3. 自动化流程拆解（一张图看懂）
![main分支的源文件结构]({photo}/branch-deploy/auto-deploy-flow.png)
1. 你在本地main分支写好文章，执行`git push origin main`，将源文件推送到GitHub的main分支；
2. GitHub检测到main分支有新推送，触发pelican.yml定义的工作流；
3. 工作流在Ubuntu环境中自动安装Python、Pelican及依赖；
4. 运行`pelican content`命令，从源文件生成静态网站到output目录；
5. 将output目录的所有文件推送到gh-pages分支；
6. GitHub Pages自动读取gh-pages分支的文件，更新博客页面（一般1-2分钟生效）。

## 三、实战：规范的博客版本管理方法（源文件+发布版本）
搞懂了分支和自动化部署后，核心是掌握「源文件版本管理」和「发布版本管理」的规范流程，避免文件混乱。

### 1. 源文件版本管理（main分支）
源文件是你的「创作素材」，必须做好版本控制，方便回滚、备份、多设备同步。
#### 核心操作步骤（本地操作）
```bash
# 1. 确保当前在main分支（如果不在，切换到main）
git checkout main

# 2. 新建/修改文章（在content目录下写.md文件）
# 例如：在content目录新建article2.md，写完文章

# 3. 查看修改的文件
git status

# 4. 将修改添加到暂存区
git add content/article2.md # 单个文件，或用git add . 添加所有修改

# 5. 提交修改（写清楚提交说明，方便后续查看）
git commit -m "添加第二篇博客：分支管理与自动化部署"

# 6. 推送到GitHub的main分支（触发自动化部署）
git push origin main
```

#### 版本管理技巧
- 每次写完一篇文章或修改配置后，及时提交（commit），提交说明要清晰（比如「修改站点标题」「添加Python教程文章」）；
- 如果需要回滚到之前的版本，用`git log`查看提交记录，找到要回滚的commit-id，执行`git reset --hard commit-id`（谨慎使用，会覆盖本地修改）；
- 多设备同步：在另一台电脑上，克隆仓库的main分支即可获取所有源文件：
  ```bash
  git clone -b main https://github.com/unclevicky/unclevicky.github.io.git
  cd unclevicky.github.io
  # 安装依赖（如果需要本地测试）
  pip install pelican markdown pelican-photos
  ```

### 2. 发布版本管理（gh-pages分支）
发布版本是生成的静态文件，完全由自动化流程管理，无需手动操作：
- 无需手动切换到gh-pages分支修改文件，所有更新都通过main分支的推送自动触发；
- 如果发布后发现问题（比如文章格式错误），只需在main分支修改源文件，重新提交推送，自动化流程会自动更新gh-pages分支的内容，覆盖旧版本；
- 如需查看历史发布版本，可在GitHub仓库的「Branches→gh-pages→Commits」中查看，也可通过`git checkout gh-pages`在本地查看（但不建议修改）。

### 3. 历史master分支的处理建议
如果master分支没有实际用途，建议清理掉，避免混淆：
```bash
# 本地删除master分支（确保已备份必要文件）
git branch -d master

# 远程删除GitHub仓库的master分支
git push origin --delete master
```
删除后，仓库只剩main（源文件）和gh-pages（发布文件）两个分支，逻辑更清晰。

### 4. 本地测试与自动化部署的配合
日常写文章时，建议先本地测试效果，再推送触发自动化部署：
```bash
# 本地生成静态文件并启动服务
pelican content
cd output
python -m pelican.server
# 访问127.0.0.1:8000查看效果，确认无误后再提交推送
```

## 四、常见问题排查
1. 推送main分支后，博客没更新？
   - 查看GitHub仓库的「Actions」标签，看pelican.yml工作流是否执行成功（绿色对勾表示成功，红色叉号表示失败）；
   - 若失败，点击查看日志，大概率是依赖安装失败或源文件语法错误（比如markdown格式错误）。

2. gh-pages分支没有自动生成？
   - 检查pelican.yml中`publish_branch`是否配置为gh-pages；
   - 检查仓库的「Settings→Pages→Source」是否选择「gh-pages分支」（如果没有，手动选择一次即可）。

3. 多设备同步时，本地修改与远程main分支冲突？
   - 先拉取远程最新版本：`git pull origin main`；
   - 解决冲突文件（打开冲突文件，按提示保留需要的内容）；
   - 再提交推送：`git commit -m "解决同步冲突" && git push origin main`。

## 结尾
理清分支分工和自动化部署逻辑后，博客维护会变得非常规范：日常只需专注在main分支写文章、改配置，提交后等待1-2分钟，GitHub Actions就会自动完成部署。main分支负责「记录创作过程」，gh-pages分支负责「展示最终效果」，两者各司其职，既不用担心源文件丢失，也不用手动处理复杂的部署步骤。

下一篇博客，我会分享Pelican主题更换、插件推荐（比如评论功能、文章搜索）等进阶技巧，让博客功能更丰富～ 如果在分支管理或自动化部署中遇到问题，欢迎在评论区留言交流！

Proudly powered by Pelican, which takes great advantage of Python.
Published: 周一 10 六月 2024 Updated: 周一 10 六月 2024 By 田冲憨娃 In 技术,教程. tags: pelican,github.io,分支管理,自动化部署,版本控制