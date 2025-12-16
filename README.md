# 04_PYTHON语言中的运算符

## 什么是 f-string？

f-string 是以字母 `f` 或 `F` 开头的字符串字面量（string literal），它里面可以包含用花括号 `{}` 包裹的表达式。

### 基本语法

Python

```
name = "爱丽丝"
age = 30
# 使用 f-string
greeting = f"你好，我的名字是 {name}，我今年 {age} 岁。"
print(greeting)
# 输出: 你好，我的名字是 爱丽丝，我今年 30 岁。
```

------

### f-string 的核心特性

#### 1. 嵌入任意 Python 表达式

花括号 `{}` 内可以放置任何有效的 Python 表达式，f-string 会在运行时计算这些表达式的值，并将结果转换为字符串。

- **变量/字面量：**

  Python

  ```
  pi = 3.14159
  print(f"圆周率的近似值是 {pi}")
  ```

- **数学运算：**

  Python

  ```
  x, y = 10, 5
  print(f"10 乘以 5 等于 {x * y}")
  ```

- **函数调用/方法调用：**

  Python

  ```
  s = "hello world"
  print(f"大写后的字符串是 {s.upper()}")
  ```

- **列表/字典访问：**

  Python

  ```
  data = {'city': '北京', 'temp': 25}
  print(f"天气预报：{data['city']} 今天的温度是 {data['temp']} 度。")
  ```

#### 2. 格式化说明符 (Format Specifiers)

f-string 继承了 `str.format()` 方法中使用的**格式化说明符**（Format Specifiers）。它允许你控制表达式结果的显示方式，例如小数精度、对齐方式、数字分隔符等。

语法结构是：`{expression:format_spec}`

| **说明符** | **描述**                     | **示例**         | **结果**     |
| ---------- | ---------------------------- | ---------------- | ------------ |
| **`.nf`**  | 浮点数保留 **n** 位小数      | `f"{1/3:.2f}"`   | `0.33`       |
| **`n`**    | **n** 为总宽度，默认为右对齐 | `f"{'hi':<10}"`  | `hi        ` |
| **`<`**    | 左对齐                       | `f"{123:<8}"`    | `123     `   |
| **`>`**    | 右对齐                       | `f"{123:>8}"`    | `     123`   |
| **`^`**    | 居中对齐                     | `f"{'C':^5}"`    | ` C `        |
| **`,`**    | 数字千位分隔符               | `f"{1234567:,}"` | `1,234,567`  |
| **`%`**    | 百分比格式                   | `f"{0.75:.0%}"`  | `75%`        |

> 💡 **示例：**
>
> Python
>
> ```
> price = 12345.678
> print(f"价格 (保留两位小数): ${price:.2f}")  # $12345.68
> print(f"价格 (千位分隔符): ${price:,.2f}") # $12,345.68
> print(f"百分比 (居中对齐): {0.45:^10.1%}")  #   45.0%
> ```

#### 3. 类型转换 (Conversion)

你可以在表达式后面使用 `!s`、`!r` 或 `!a` 来强制执行类型转换：

- `!s`：调用 `str()`，即对象的**字符串表示**。
- `!r`：调用 `repr()`，即对象的**正式表示**（通常用于调试）。
- `!a`：调用 `ascii()`，即对象的 **ASCII 格式**。

Python

```
class MyClass:
    def __repr__(self):
        return '正式表示'
    def __str__(self):
        return '字符串表示'

obj = MyClass()
print(f"默认/!s: {obj!s}") # 字符串表示
print(f"!r (调试): {obj!r}") # 正式表示
```

------

###  f-string 的注意事项

- **引号冲突：** 如果 f-string 使用单引号 `'`，则内部表达式中字符串必须使用双引号 `"`，反之亦然。或者使用三引号 `"""` 来避免冲突。

  Python

  ```
  # 错误: f'It's {value}'
  print(f"It's {data['key']}") # 正确
  ```

- **反斜杠：** 花括号内部的表达式不能包含反斜杠字符 `\`（除了用于转义引号）。

- **大括号：** 如果需要在 f-string 中显示字面量大括号 `{}`，需要使用双层大括号 `{{` 和 `}}` 来转义。

  Python

  ```
  print(f"字典的键值对格式：{{'key': value}}")
  # 输出: 字典的键值对格式：{'key': value}
  ```

------



f-string 的**引号冲突**和**大括号转义**是初学者经常遇到的问题。我将使用更具体的例子来详细解释这两点，让您彻底理解。

------

#### 1. f-string 的引号冲突（Quote Conflicts）

f-string 本身是用引号（单引号 `'` 或双引号 `"`）包起来的字符串字面量。当你在 f-string 内部的表达式中需要使用**字符串**时，就会发生引号冲突。

##### 冲突的原理

1. **外部引号 (Outer Quotes)：** 定义 f-string 的引号，例如：`f"..."` 或 `f'...'`。
2. **内部引号 (Inner Quotes)：** f-string **花括号 `{}` 内部** Python 表达式中使用的引号。

**规则：** 外部引号和内部引号**不能是同一种类型**。

| **外部引号** | **内部引号 (正确)** | **内部引号 (错误: 冲突!)** |
| ------------ | ------------------- | -------------------------- |
| `f" ... "`   | 使用 `'...'`        | 使用 `"..."`               |
| `f' ... '`   | 使用 `"..."`        | 使用 `'...'`               |

#####  示例分析

######  错误示例 (冲突)

假设你有一个字典 `data = {'city': '北京'}`，你想在 f-string 中访问键 `'city'`：

Python

```
data = {'city': '北京'}

# f-string 使用双引号 "，表达式中的键也使用双引号 "
# Python 会提前终止 f-string，导致语法错误。
# code = f"今天的城市是 {data["city"]}" # <-- 这里的 " 被认为是 f-string 的结束引号
```

######  正确示例 (避免冲突)

要解决这个问题，只需要让内部的引号与外部的引号**不同**即可：

Python

```
data = {'city': '北京'}

# 方案一：外部用双引号，内部用单引号
result1 = f"今天的城市是 {data['city']}"
print(f"方案一结果: {result1}")
# 输出: 今天的城市是 北京

# 方案二：外部用单引号，内部用双引号
result2 = f'今天的城市是 {data["city"]}'
print(f"方案二结果: {result2}")
# 输出: 今天的城市是 北京
```

######  最佳实践：三引号 `"""`

如果你的 f-string 内容很长，或者需要内嵌**单引号和双引号**（例如包含 HTML 或 JSON），可以使用**三引号** (`"""..."""` 或 `'''...'''`) 作为外部引号，这样可以无限制地在内部使用单引号和双引号，彻底避免冲突。

Python

```
html_tag = "<h1>标题</h1>"
print(f"""这是一个包含 "双引号" 的字符串，它里面有 {html_tag}，也可以有 '单引号'。""")
```

------

#### 2. f-string 的大括号转义（Brace Escaping）

f-string 使用 `{` 和 `}` 来界定需要计算的 Python 表达式。如果你想在最终的输出字符串中**显示字面量的大括号**，而不是让 Python 将其解释为表达式的起始和结束标记，你就需要进行转义。

##### 转义的原理

要显示一个字面量的大括号，你需要使用**双层大括号**：`{{` 代表 `{`，`}}` 代表 `}`。

##### 示例分析

错误示例 (被解析为表达式)

如果你只使用单层大括号，Python 会认为这是一个表达式，但里面是空的，或者不是一个有效的 Python 表达式，从而报错：

Python

```
# print(f"这是一个字典的格式：{'key': value}") # 错误的，f-string会解析里面的 :

# 错误示例：试图打印字面量大括号
# print(f"我需要打印一个开括号：{")  # SyntaxError
```

正确示例 (转义)

使用双层大括号 `{{` 和 `}}` 告诉 Python ：“这不是一个表达式，请把它当作一个普通字符打印出来。”

Python

```
name = "小明"

# 使用双层大括号打印字面量的大括号
output1 = f"你好，这是一个 {name} 的示例：{{'name': '小明'}}"
print(f"示例一：{output1}")
# 输出: 你好，这是一个 小明 的示例：{'name': '小明'}

# 如果你想打印一个空的表达式占位符 {}
output2 = f"这是一个空的占位符：{{}}"
print(f"示例二：{output2}")
# 输出: 这是一个空的占位符：{}
```

###### 结合使用

在一个 f-string 中，你可以同时拥有：

1. **计算表达式**（单层大括号）：`{expression}`
2. **打印字面量大括号**（双层大括号）：`{{` 或 `}}`

Python

```
score = 95
print(f"我的分数是 {score}，它的格式是 {{'score': {score}}}")
# 解析过程：
# 1. {score} -> 95
# 2. {{ -> {
# 3. }} -> }
# 最终输出: 我的分数是 95，它的格式是 {'score': 95}
```



## f-string 优于其他方法的优势

在 Python 中，字符串格式化还有 `str.format()` 和传统的 `%` 运算符，但 f-string 是官方推荐的现代方法。

| **特性**       | **f-string (Python 3.6+)** | **str.format()**            | **% 运算符 (Old School)** |
| -------------- | -------------------------- | --------------------------- | ------------------------- |
| **语法简洁性** | 极高，直接嵌入表达式       | 中等，使用 `{}`, 需传入参数 | 较低，使用 `%s`, `%d`     |
| **可读性**     | 很高，变量直接可见         | 中等，变量与占位符分离      | 较低，需对照占位符类型    |
| **性能**       | 最快 (编译时处理)          | 较慢                        | 最慢                      |
| **表达式支持** | **支持任意表达式**         | 不支持，仅支持参数占位符    | 不支持，仅支持参数占位符  |



# 05_分支结构

## 语法：

​	if (条件):

```
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
```

​	if (条件):

​	else:

```
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
else:
    print('你的身材不够标准哟！')
```

​	if (条件):

​	elif (条件):

​	...

​	elif (条件):

​	else:

```
status_code = int(input('响应状态码: '))
if status_code == 400:
    description = 'Bad Request'
elif status_code == 401:
    description = 'Unauthorized'
elif status_code == 403:
    description = 'Forbidden'
elif status_code == 404:
    description = 'Not Found'
elif status_code == 405:
    description = 'Method Not Allowed'
elif status_code == 418:
    description = 'I am a teapot'
elif status_code == 429:
    description = 'Too many requests'
else:
    description = 'Unknown status Code'
print('状态码描述:', description)
```

​	match (变量):

​	case 变量值：

​	...

​	case 变量值：

​	case _:

```
status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
```



```
status_code = int(input('响应状态码: '))
match status_code:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
```