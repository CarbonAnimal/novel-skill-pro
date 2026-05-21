# 封面设计指南

## 封面生成流程

1. 解析书名 + 题材 → 确定视觉风格
2. 生成封面提示词
3. 调用图像生成模型出图
4. 展示 2-3 个候选方案给用户选择

---

## 10大题裁视觉风格

| 题材 | 主色调 | 风格关键词 | 构图特点 |
|------|--------|----------|---------|
| **悬疑推理** | 暗蓝/深灰/血红 | 压抑、神秘、冷峻 | 暗光剪影、局部特写、负空间 |
| **玄幻修仙** | 金/紫/青蓝 | 大气、仙侠、东方幻想 | 纵深感强、云海山峰、人物小比例 |
| **都市言情** | 暖粉/雾蓝/奶油 | 温柔、浪漫、现代感 | 双人构图、背影/侧脸、街头氛围 |
| **古言权谋** | 朱红/墨黑/金色 | 华丽、复古、厚重 | 对称构图、纹饰边框、宫廷元素 |
| **科幻末世** | 冷蓝/银灰/荧光绿 | 未来感、冷硬、宏大 | 科技元素、废墟/城市、赛博朋克 |
| **奇幻异世** | 紫红/墨绿/暗金 | 神秘、空灵、魔幻 | 异世界风景、魔法元素、非人角色 |
| **恐怖灵异** | 黑/暗红/惨白 | 惊悚、诡异、不安 | 局部恐怖特写、负空间、隐喻符号 |
| **轻松甜宠** | 粉/薄荷绿/淡紫 | 清新、可爱、治愈 | 插画风格、明亮色调、可爱元素 |
| **历史军事** | 棕褐/军绿/铁灰 | 厚重、铁血、沧桑 | 战场/古城、冷兵器/军械、旗帜 |
| **短篇文艺** | 暖黄/墨蓝/留白 | 意境、简洁、情绪化 | 大面积留白、单元素构图、极简 |

---

## 提示词模板

### 通用结构
```
[题材风格描述], [主体元素], [氛围], [构图], [色调], [画质要求]
```

### 悬疑示例
```
dark suspense thriller book cover, a lone figure standing at an empty subway platform,
mysterious shadows, cold blue and deep gray tones, negative space composition,
cinematic lighting, minimalist design, book cover layout, 8K quality
```

### 言情示例
```
romantic contemporary book cover, couple silhouettes walking under cherry blossoms,
warm pink and misty blue tones, soft dreamy atmosphere, golden hour lighting,
elegant typography space on top, book cover design, high quality
```

### 玄幻示例
```
epic xianxia fantasy book cover, lone cultivator standing on mountain peak overlooking cloud sea,
golden light breaking through clouds, traditional Chinese ink wash style blended with fantasy,
purple and gold color palette, majestic atmosphere, book cover with title space, ultra detailed
```

---

## 封面检查清单

- [ ] 风格与题材匹配？
- [ ] 色调是否形成视觉冲击力？
- [ ] 是否有足够的留白放书名？
- [ ] 小尺寸（缩略图）下是否仍然可识别？
- [ ] 是否避免了低质量/模糊/奇怪的人体结构？
