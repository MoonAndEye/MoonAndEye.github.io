---
layout: post
title: Swiftformat 在設定 swiftversion 5.7，會把 T 改成 some Any
date: 2023-03-17 09:12 +0800
category: swift
author: Marvin Lin
tags: [swift]
summary: 
---

## Swiftformat 可調整的各種參數

swiftformat 在進行 formatting  的時候，有很多參數可以調整。詳細的參數如下。

[swiftformat 參數連結](https://github.com/nicklockwood/SwiftFormat/blob/master/.swiftformat)

```
# file options

--exclude Tests/XCTestManifests.swift,Tests/BadConfig,Snapshots,Build,PluginTests

# format options

--allman false
--binarygrouping 4,8
--commas always
--decimalgrouping 3,6
--elseposition same-line
--voidtype void
--exponentcase lowercase
--exponentgrouping disabled
--fractiongrouping disabled
--header ignore
--hexgrouping 4,8
--hexliteralcase uppercase
--ifdef indent
--indent 4
--indentcase false
--importgrouping testable-bottom
--linebreaks lf
--maxwidth none
--octalgrouping 4,8
--operatorfunc spaced
--patternlet hoist
--ranges spaced
--self remove
--semicolons inline
--stripunusedargs always
--swiftversion 5.1
--trimwhitespace always
--wraparguments preserve
--wrapcollections preserve

# rules

--enable isEmpty
```

當我們把 `--swiftversion 5.1` 調整到 `--swiftversion 5.7` 的時候，使用泛型 T，就會被改成 some Any。

```
// --swiftversion 5.1 ~ 5.6
func log<T>(_ message: T) {

// --swiftversion 5.7
func log(_ message: some Any) {
```

如果仍然不希望 swiftformat 改動 T，那可以在 `.swiftformat` 中，加上 disable，`--disable opaqueGenericParameters`。這樣就不會讓 T 改成 some Any 了。