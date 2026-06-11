<!-- source: https://platform.kimi.com/docs/overview -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 欢迎使用 Kimi API 文档

<div className="overview-page not-prose" style={{ display: 'flex', flexDirection: 'column', gap: '32px' }}>
  <div className="overview-hero-card" style={{ position: 'relative', overflow: 'hidden', borderRadius: '16px', border: '1px solid rgba(200, 200, 200, 0.4)' }}>
    <video autoPlay loop muted playsInline src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/moonshot-ai/k2-video.mp4?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=af8b3482eddad898243ae40932757334" style={{ width: '100%', height: '100%', display: 'block', margin: 0, padding: 0, aspectRatio: '813/295', objectFit: 'cover', verticalAlign: 'bottom' }} data-path="assets/moonshot-ai/k2-video.mp4" />

    <div style={{ position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column', justifyContent: 'flex-end', background: 'linear-gradient(to top, rgba(0,0,0,0.7), rgba(0,0,0,0.3), transparent)', padding: '24px' }}>
      <div style={{ display: 'flex', gap: '16px', alignItems: 'flex-end', justifyContent: 'space-between' }}>
        <div style={{ flex: 1 }}>
          <div style={{ color: 'white', fontSize: '24px', fontWeight: 600 }}>Kimi K2.6 模型</div>

          <div style={{ color: 'rgba(255,255,255,0.7)', fontSize: '14px', marginTop: '4px', maxWidth: '600px' }}>
            Kimi K2.6 是 Kimi 最新最智能的模型，具备更强更稳的长程代码编写能力，同时支持文本、图片与视频输入，支持256K上下文长度
          </div>
        </div>

        <a href="https://platform.kimi.com/console/api-keys" className="overview-hero-card__cta">
          申请 API Key →
        </a>
      </div>
    </div>

    <a href="pricing/chat-k26" style={{ position: 'absolute', inset: 0, zIndex: 5, textDecoration: 'none', border: 'none' }} aria-label="Kimi K2.6: 新一代多模态模型" />
  </div>

  <div>
    <h2 style={{ fontSize: '24px', fontWeight: 600, marginBottom: '16px' }}>快速开始</h2>

    <div className="overview-grid-2">
      {[
                  { title: "Kimi K2.6 快速开始", desc: "接入 Kimi K2.6 多模态模型", icon: "bolt", href: "/guide/kimi-k2-6-quickstart" },
                  { title: "控制台", desc: "管理 API Key、查看用量和账单", icon: "chart-line", href: "https://platform.kimi.com/console" },
                  { title: "促销活动", desc: "查看限时充值优惠活动", icon: "handshake", href: "/pricing/promotion" },
                  { title: "价格与计费", desc: "了解各个模型的价格与计费方式", icon: "wallet", href: "/pricing/chat" },
                  { title: "使用 Thinking 模型", desc: "了解如何使用 Kimi 模型的思考能力", icon: "clock", href: "/guide/use-kimi-k2-thinking-model" },
                  { title: "常见问题", desc: "查看常见问题解答", icon: "circle-question", href: "/guide/faq" },
                ].map((item, idx) => (
                  <div key={idx} className="overview-link-card">
                    <div className="overview-link-card__body">
                      <div className="overview-link-card__icon">
                        <Icon icon={item.icon} size={20} />
                      </div>
                      <div className="overview-link-card__content">
                        <div className="overview-link-card__title">{item.title}</div>
                        <div className="overview-link-card__description">{item.desc}</div>
                      </div>
                    </div>
                    <a className="overview-overlay-link" href={item.href} aria-label={item.title} />
                  </div>
                ))}
    </div>
  </div>

  <div>
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '16px' }}>
      <h2 style={{ fontSize: '24px', fontWeight: 600, margin: 0 }}>模型及定价</h2>
      <a href="pricing/chat" className="overview-section-link" style={{ fontSize: '14px' }}>查看全部</a>
    </div>

    <div className="overview-grid-3">
      {[
                  { name: "kimi-k2.6", img: "assets/moonshot-ai/report5.png", tag: "多模态理解", href: "/pricing/chat-k26" },
                  { name: "kimi-k2.5", img: "assets/moonshot-ai/report2.png", tag: "多模态理解", href: "/pricing/chat-k25" },
                  { name: "moonshot-v1-128k", img: "assets/moonshot-ai/k2-0905.png", tag: "v1 系列", href: "/pricing/chat-v1" },
                ].map((item, idx) => (
                  <div key={idx} className="overview-model-card">
                    <div className="overview-model-card__media" style={{ position: 'relative' }}>
                      <img className="overview-model-card__image" src={item.img} alt={item.name} />
                      <div className="overview-model-card__overlay" style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'flex-end' }}>
                        <div className="overview-model-card__content">
                          <div className="overview-model-card__name">{item.name}</div>
                          <div className="overview-model-card__tag-row">
                            <span style={{ border: '1px solid rgba(255,255,255,0.3)', color: 'rgba(255,255,255,0.9)', padding: '2px 8px', borderRadius: '9999px', fontSize: '12px', background: 'rgba(0,0,0,0.2)' }}>
                              {item.tag}
                            </span>
                          </div>
                        </div>
                      </div>
                    </div>
                    <a className="overview-overlay-link" href={item.href} aria-label={item.name} />
                  </div>
                ))}
    </div>
  </div>

  <div>
    <h2 style={{ fontSize: '24px', fontWeight: 600, marginBottom: '16px' }}>更多资源</h2>

    <div className="overview-grid-4">
      {[
                  { title: "Kimi K2.6 模型详解", desc: "查看 K2.6 模型报告，了解 K2.6 模型的特性与优势", icon: "brain", href: "https://www.kimi.com/blog/kimi-k2-6" },
                  { title: "开发工作台", desc: "通过界面交互式体验 Kimi 模型的能力", icon: "terminal", href: "https://platform.kimi.com/playground" },
                  { title: "联网搜索工具", desc: "使用 Kimi 官方联网搜索工具", icon: "magnifying-glass", href: "/guide/use-web-search" },
                  { title: "最佳实践", desc: "提示词编写与应用案例", icon: "file-lines", href: "/guide/prompt-best-practice" },
                ].map((item, idx) => (
                  <div key={idx} className="overview-resource-card">
                    <div className="overview-resource-card__body">
                      <div className="overview-link-card__icon">
                        <Icon icon={item.icon} size={20} />
                      </div>
                      <div className="overview-link-card__content">
                        <div className="overview-resource-card__title">{item.title}</div>
                        <div className="overview-resource-card__description">{item.desc}</div>
                      </div>
                    </div>
                    <a className="overview-overlay-link" href={item.href} aria-label={item.title} />
                  </div>
                ))}
    </div>
  </div>
</div>
