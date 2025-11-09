# 💝 浪漫弹窗网站 - GitHub Pages部署指南

## 🌐 网站地址修改说明

### 当前网站地址格式
```
https://[你的GitHub用户名].github.io/[仓库名称]
```

### 📍 修改网站地址的方法

#### 方法1：修改仓库名称（推荐）
1. 进入你的GitHub仓库页面
2. 点击 **Settings** 标签
3. 在 **Repository name** 字段修改仓库名称
4. 点击 **Rename** 确认
5. 新的网站地址将自动更新为：
   ```
   https://[你的GitHub用户名].github.io/[新仓库名称]
   ```

#### 方法2：使用自定义域名（高级）
1. 在仓库中创建 `CNAME` 文件
2. 在文件中写入你的自定义域名，如：
   ```
   love.example.com
   ```
3. 在你的域名DNS设置中添加CNAME记录指向：
   ```
   [你的GitHub用户名].github.io
   ```

### 🎯 示例修改
- **原地址**：`https://username.github.io/love-website`
- **修改后**：`https://username.github.io/my-love-page`

### ⚡ 注意事项
- 地址修改后，旧的链接将失效
- 修改仓库名称不会影响已部署的网站内容
- 自定义域名需要拥有自己的域名并配置DNS

## 🚀 快速部署步骤

### 1. 创建GitHub仓库
- 登录GitHub，点击 **New repository**
- 仓库名称建议使用：`love-website` 或其他你喜欢的名称
- 设置为 **Public**
- 不要勾选 **Initialize this repository with a README**

### 2. 上传代码
```bash
git init
git add .
git commit -m "Initial commit: Love popup website"
git branch -M main
git remote add origin https://github.com/[你的用户名]/[仓库名称].git
git push -u origin main
```

### 3. 启用GitHub Pages
- 进入仓库页面，点击 **Settings**
- 左侧菜单选择 **Pages**
- **Source** 选择 **Deploy from a branch**
- **Branch** 选择 **main** 和 **/(root)**
- 点击 **Save**

### 4. 访问网站
等待1-2分钟后，访问：
```
https://[你的GitHub用户名].github.io/[仓库名称]
```

## 📁 项目文件说明
- `index.html` - 主页面文件
- `.gitignore` - Git忽略文件配置
- `.inscode` - 部署配置文件
- `README.md` - 本说明文档

## 🎨 个性化定制
- 修改 `index.html` 中的文案内容
- 调整弹窗颜色和样式
- 添加更多浪漫元素

## 💡 常见问题
**Q: 修改仓库名称后需要重新部署吗？**
A: 不需要，GitHub会自动更新地址

**Q: 可以修改GitHub用户名吗？**
A: 可以，但会影响所有GitHub Pages的地址

**Q: 网站多久能生效？**
A: 通常1-2分钟，最长不超过10分钟

---

💖 祝你的网站充满爱意！