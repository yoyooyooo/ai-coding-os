# AI Coding OS Suite Contract Snapshot

本目录是 `$evolvable-application-preset` 自带的命名默认值快照，来源语义由
`$ai-coding-os-suite-contracts` 拥有。

Preset 必须能在独立安装、Skill 目录被打平时运行，因此 renderer 只读取本 Skill
内部的固定快照，不跨目录查找其他 Skill。Suite source audit 会校验该快照与
`$ai-coding-os-suite-contracts` 当前发布源一致；升级 Preset 时必须显式刷新快照和
golden output。

渲染后的项目 Standards 才是项目当前权威，本快照不是动态继承面。
