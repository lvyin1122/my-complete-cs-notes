# HTML DOM

The HTML DOM model is constructed as a tree of Objects

## 1. DOM Methods

- actions
- values

### The DOM Programming Interface

defined as objects

property

method

```html
<html>
<body>

<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = "Hello World!";
</script>

</body>
</html>
```

- The getElementById Method
- innerHTML Property

## 2. HTML DOM Document Object

### Finding HTML Elements

- document.getElementById(id)
- document.getElementByTagName(name)
- document.getElementByClassName(name)

### Changing HTML Elements

```js
element.innerHTML = new html content
element.attribute = new value
element.style.property = new style
element.setAttribute(attribute, value)
```

### Adding Events Handlers

```js
document.getElementById(id).onclick = function(){code}
```

## 3. JavaScript HTML DOM Elements

