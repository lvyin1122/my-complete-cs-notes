# DOCS-01: Step-by-step Tutorial

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



## 3. 