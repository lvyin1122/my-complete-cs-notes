# DOCS-01: Step-by-step Tutorial

This file includes ch1-3

## 1. Hello World

```js
ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('root')
);
```

## 2. JSX

```js
const name = 'Josh Perex';
const element = <h1>Hello, {name}</h1>;

ReactDOM.render(
    element,
    document.getElementById('root')
)
```

```js
function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const user = {
  firstName: 'Harper',
  lastName: 'Perez'
};

const element = (
  <h1>
    Hello, {formatName(user)}!
  </h1>
);

ReactDOM.render(
  element,
  document.getElementById('root')
);
```

JSX is an Expression Too

```js
function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;
  }
  return <h1>Hello, Stranger.</h1>;
}
```

Specifying Attributes with JSX

```js
const element = <div tabIndex="0"></div>;

const element = <img src={user.avatarUrl}></img>
```

Specifying Children with JSX

```js
const element = <img src={user.avatarUrl} />;

const element = (
  <div>
    <h1>Hello!</h1>
    <h2>Good to see you here.</h2>
  </div>
);
```

Other

```js
// Prevents Injection Attacks
const title = response.potentiallyMaliciousInput;
// This is safe:
const element = <h1>{title}</h1>;

// Represents Objects
const element = (
  <h1 className="greeting">
    Hello, world!
  </h1>
);

const element = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);
// performs a few checks to help
// it creates an object like this:
const element = {
  type: 'h1',
  props: {
    className: 'greeting',
    children: 'Hello, world!'
  }
};

```

## 3. Rendering Elements

```html
<div id="root"></div>
```
```js
const element = <h1>Hello, world</h1>;
ReactDOM.render(element, document.getElementById('root'));
```
Updating the Rendered Element

create new element and pass it to render()

```js
function tick(){
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(element, document.getElementById('root'));
}

setInterval(tick, 1000);
```
React only updates what's necessary

