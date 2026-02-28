# Node.js


<!-- TOC START -->
- [Related Terms:](#related-terms)
  - [See also:](#see-also)
- [Questions about Node.js ?](#questions-about-nodejs)
  - [Basics and Importance](#basics-and-importance)
    - [What is Node.js and why is it important?](#what-is-nodejs-and-why-is-it-important)
    - [What is the difference between Node.js and JavaScript?](#what-is-the-difference-between-nodejs-and-javascript)
    - [What are the key features of Node.js?](#what-are-the-key-features-of-nodejs)
    - [Why is Node.js single-threaded?](#why-is-nodejs-single-threaded)
    - [What is the event-driven programming in Node.js?](#what-is-the-event-driven-programming-in-nodejs)
  - [Working with Node.js](#working-with-nodejs)
    - [How do you install Node.js on your system?](#how-do-you-install-nodejs-on-your-system)
    - [How do you update Node.js?](#how-do-you-update-nodejs)
    - [How can you debug a Node.js application?](#how-can-you-debug-a-nodejs-application)
    - [What is NPM and how is it used in Node.js?](#what-is-npm-and-how-is-it-used-in-nodejs)
    - [How do you create a server in Node.js?](#how-do-you-create-a-server-in-nodejs)
  - [Node.js Modules](#nodejs-modules)
    - [What are modules in Node.js?](#what-are-modules-in-nodejs)
    - [How do you create and use a module in Node.js?](#how-do-you-create-and-use-a-module-in-nodejs)
    - [What are some of the built-in modules in Node.js?](#what-are-some-of-the-built-in-modules-in-nodejs)
    - [What is the purpose of module.exports in Node.js?](#what-is-the-purpose-of-moduleexports-in-nodejs)
    - [How do you include third-party modules in a Node.js application?](#how-do-you-include-third-party-modules-in-a-nodejs-application)
  - [Node.js and Databases](#nodejs-and-databases)
    - [How do you connect a Node.js application to a database?](#how-do-you-connect-a-nodejs-application-to-a-database)
    - [How do you perform CRUD operations in Node.js?](#how-do-you-perform-crud-operations-in-nodejs)
    - [What is ORM and how is it used in Node.js?](#what-is-orm-and-how-is-it-used-in-nodejs)
    - [How do you handle database errors in Node.js?](#how-do-you-handle-database-errors-in-nodejs)
  - [Advanced Concepts](#advanced-concepts)
    - [What is the event loop in Node.js?](#what-is-the-event-loop-in-nodejs)
    - [What is callback hell and how can you avoid it in Node.js?](#what-is-callback-hell-and-how-can-you-avoid-it-in-nodejs)
    - [What are promises and async/await in Node.js?](#what-are-promises-and-asyncawait-in-nodejs)
    - [What is the cluster module in Node.js and why is it useful?](#what-is-the-cluster-module-in-nodejs-and-why-is-it-useful)
    - [How does Node.js handle child processes?](#how-does-nodejs-handle-child-processes)
<!-- TOC END -->

Node.js

is an open-source, cross-platform JavaScript runtime environment that allows developers to execute JavaScript code server-side. Traditionally, JavaScript was primarily used for client-side scripting in web browsers.

Node.js

, however, enables JavaScript to be used for building scalable network applications outside the browser. Built on Chrome's V8 JavaScript engine,

Node.js

is designed for building fast and efficient web applications, especially I/O-bound applications.

## Related Terms:

- [JavaScript runtime](../J/javascript-runtime.md)
- [Jest](../J/jest.md)
- [Jasmine](../J/jasmine.md)

### See also:

- [Official Website](https://nodejs.org/)
- [Wikipedia](https://en.wikipedia.org/wiki/Node.js)

## Questions about Node.js ?

### Basics and Importance

#### What is Node.js and why is it important?

  [Node.js](../N/node-js.md) is an open-source, cross-platform runtime environment that allows you to run JavaScript on the server side. It's built on Chrome's V8 JavaScript engine, and it enables developers to use JavaScript to write command-line tools and server-side scripting—running scripts server-side to produce dynamic web page content before the page is sent to the user's web browser.
  **Importance of [Node.js](../N/node-js.md):**

  - **Unified Language**: [Node.js](../N/node-js.md) uses JavaScript, which means the same language can be used on both the client and server sides. This simplifies development and can lead to increased efficiency and understanding across teams.
  - **Asynchronous I/O**: It handles I/O operations asynchronously, which can lead to better performance and scalability, especially for applications that require heavy I/O operations, such as [test automation](../T/test-automation.md) systems that may need to handle multiple tasks concurrently.
  - **NPM Ecosystem**: [Node.js](../N/node-js.md) comes with npm (Node Package Manager), a massive repository of libraries and tools, which can be extremely beneficial for [test automation](../T/test-automation.md), providing a wealth of modules to extend functionality and reduce development time.
  - **Microservices Architecture**: It is well-suited for building microservices, which are a popular architectural style for building scalable systems, including [test automation](../T/test-automation.md) frameworks that may need to integrate with various services and tools.
  - **Cross-Platform**: [Node.js](../N/node-js.md) applications can run on various operating systems without modification, making it an ideal choice for [test automation](../T/test-automation.md) tools that need to be platform-agnostic.
  - **Community and Support**: It has a large and active community, which means a wealth of resources, support, and continuous improvements to the technology, which can be advantageous for maintaining and updating [test automation](../T/test-automation.md) frameworks.
  - **Unified Language**: [Node.js](../N/node-js.md) uses JavaScript, which means the same language can be used on both the client and server sides. This simplifies development and can lead to increased efficiency and understanding across teams.
  - **Asynchronous I/O**: It handles I/O operations asynchronously, which can lead to better performance and scalability, especially for applications that require heavy I/O operations, such as [test automation](../T/test-automation.md) systems that may need to handle multiple tasks concurrently.
  - **NPM Ecosystem**: [Node.js](../N/node-js.md) comes with npm (Node Package Manager), a massive repository of libraries and tools, which can be extremely beneficial for [test automation](../T/test-automation.md), providing a wealth of modules to extend functionality and reduce development time.
  - **Microservices Architecture**: It is well-suited for building microservices, which are a popular architectural style for building scalable systems, including [test automation](../T/test-automation.md) frameworks that may need to integrate with various services and tools.
  - **Cross-Platform**: [Node.js](../N/node-js.md) applications can run on various operating systems without modification, making it an ideal choice for [test automation](../T/test-automation.md) tools that need to be platform-agnostic.
  - **Community and Support**: It has a large and active community, which means a wealth of resources, support, and continuous improvements to the technology, which can be advantageous for maintaining and updating [test automation](../T/test-automation.md) frameworks.

#### What is the difference between Node.js and JavaScript?

  JavaScript is a **programming language** that runs in web browsers as part of the document object model (DOM), enabling dynamic content and interactive web pages. It's the scripting language of the web, designed to be lightweight and versatile.
  [Node.js](../N/node-js.md), on the other hand, is a **runtime environment** that allows JavaScript to be executed on the server side. It's built on Chrome's V8 JavaScript engine and enables JavaScript to perform operations typically reserved for backend languages, like file system access and network communication.
  The key difference lies in their **execution environments** and **applications**. JavaScript traditionally runs in browsers and manipulates web page content, responding to user interactions. [Node.js](../N/node-js.md) runs on a server, not in a browser, and is used to build scalable network applications.
  [Node.js](../N/node-js.md) also provides a **non-blocking I/O model** and **asynchronous programming**, which are not inherent to JavaScript itself but are part of the [Node.js](../N/node-js.md) runtime.
  Here's a simple analogy in code:

  ```
  // JavaScript in a browser
  document.getElementById('button').addEventListener('click', function() {
    alert('Button clicked!');
  });
  // Node.js on a server
  const http = require('http');
  http.createServer((request, response) => {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end('Hello World\n');
  }).listen(3000);
  ```
  In summary, JavaScript is the language, while [Node.js](../N/node-js.md) is a platform that extends JavaScript's capabilities to non-browser environments.

#### What are the key features of Node.js?

  [Node.js](../N/node-js.md) offers a **non-blocking I/O [API](../A/api.md)** that optimizes an application's throughput and scalability for real-time web applications. Its **asynchronous event-driven architecture** ensures that [Node.js](../N/node-js.md) can handle numerous simultaneous connections efficiently.
  The **libuv library** underpins [Node.js](../N/node-js.md), providing a cross-platform set of I/O primitives. [Node.js](../N/node-js.md) is built on **V8 JavaScript runtime**, which is known for its speed and performance.
  **Streams** are a collection of data – like arrays or strings, that you can read from, or write to asynchronously. [Node.js](../N/node-js.md) uses streams to handle data in chunks, which is efficient for handling large volumes of data, such as files or network communications.
  [Node.js](../N/node-js.md) has a **package ecosystem** known as npm, which is the largest ecosystem of open source libraries in the world. It allows for easy sharing and reuse of code.
  The **REPL (Read-Eval-Print Loop)** is a tool for testing [Node.js](../N/node-js.md)/JavaScript code. It's an interactive shell that processes [Node.js](../N/node-js.md) expressions. The environment allows for rapid prototyping and debugging.
  [Node.js](../N/node-js.md) supports **buffer and caching** of data, which is a temporary holding spot for data being transferred from one place to another. This improves the performance of I/O operations.
  Lastly, [Node.js](../N/node-js.md) has a **unified [API](../A/api.md)** for server-side and client-side scripting. This means that the same patterns and methods are often used for both, which can simplify the development process for isomorphic applications.

#### Why is Node.js single-threaded?

  [Node.js](../N/node-js.md) is designed to be **single-threaded** to optimize for **performance** and **scalability** in web environments. This architecture allows [Node.js](../N/node-js.md) to handle numerous concurrent connections with low overhead. A single-threaded event loop, central to [Node.js](../N/node-js.md), can manage many connections because it executes non-blocking I/O operations, meaning the server can continue processing other tasks while waiting for I/O operations to complete.
  The single-threaded model also simplifies development because it eliminates the complexity associated with thread management and synchronization. Developers don't need to worry about **deadlocks** or **race conditions** that are common in multi-threaded environments.
  However, [Node.js](../N/node-js.md) isn't limited to a single thread; it uses **worker threads** for tasks like file system operations or heavy computation, ensuring these don't block the main event loop. The **cluster module** allows running multiple [Node.js](../N/node-js.md) worker processes that can share server ports, enabling load balancing over multiple CPU cores.
  Here's an example of using the cluster module:

  ```
  const cluster = require('cluster');
  const http = require('http');
  const numCPUs = require('os').cpus().length;
  if (cluster.isMaster) {
    for (let i = 0; i < numCPUs; i++) {
      cluster.fork();
    }
  } else {
    http.createServer((req, res) => {
      res.writeHead(200);
      res.end('Hello World\n');
    }).listen(8000);
  }
  ```
  In this code, the `cluster.isMaster` check determines if the current process is the master process, which then forks worker processes. Each worker creates an HTTP server listening on the same port.

#### What is the event-driven programming in Node.js?

  Event-driven programming in [Node.js](../N/node-js.md) is a paradigm where the flow of the program is determined by events such as user actions, sensor outputs, or message passing from other programs. In [Node.js](../N/node-js.md), this is facilitated by the **EventEmitter** class, part of the **events** module, which is one of [Node.js](../N/node-js.md)'s built-in modules.
  Event-driven programming is particularly well-suited for I/O-heavy tasks, which are common in web servers and real-time applications. [Node.js](../N/node-js.md) uses this model to handle asynchronous operations, allowing it to perform non-blocking I/O tasks.
  Here's a basic example of event-driven programming in [Node.js](../N/node-js.md):

  ```
  const EventEmitter = require('events');
  class MyEmitter extends EventEmitter {}
  const myEmitter = new MyEmitter();
  myEmitter.on('event', () => {
    console.log('An event occurred!');
  });
  myEmitter.emit('event');
  ```
  In this snippet, `MyEmitter` is an extension of `EventEmitter`. We instantiate `myEmitter`, then use the `.on()` method to listen for an 'event' event. When `myEmitter.emit('event')` is called, the callback function attached to that event is executed, logging 'An event occurred!' to the console.
  This pattern is essential for handling tasks that are not completed immediately, such as reading files, making HTTP requests, or querying a [database](../D/database.md). By responding to events, [Node.js](../N/node-js.md) can continue executing other code rather than waiting, which is a key aspect of its non-blocking nature. This approach is crucial for [test automation](../T/test-automation.md) engineers to understand, as it influences how tests and assertions are structured and executed in an asynchronous environment.

### Working with Node.js

#### How do you install Node.js on your system?

  To install **[Node.js](../N/node-js.md)** on your system, follow these platform-specific instructions:
  ### For Windows and macOS:

  1. Visit the official Node.js website at
    [nodejs.org](https://nodejs.org/)
    .

  2. Click on the
    **LTS**
    (Long Term Support) or
    **Current**
    version download button, as per your requirement.

  3. Run the downloaded installer and follow the prompts to complete the installation.
  ### For Ubuntu-based distributions:
  Open your terminal and run the following commands:

  ```
  curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  sudo apt-get install -y nodejs
  ```
  Replace `14.x` with the version you wish to install.
  ### For CentOS, Fedora, and Red Hat-based distributions:
  Execute these commands in your terminal:

  ```
  curl -sL https://rpm.nodesource.com/setup_14.x | sudo bash -
  sudo yum install nodejs
  ```
  Again, replace `14.x` with the desired version.
  ### For Arch Linux:
  Use the package manager `pacman` to install [Node.js](../N/node-js.md):

  ```
  sudo pacman -S nodejs npm
  ```
  ### Verification:
  After installation, verify the installation by checking the version of [Node.js](../N/node-js.md) and npm:

  ```
  node -v
  npm -v
  ```
  This will output the installed versions of [Node.js](../N/node-js.md) and npm, confirming a successful installation.

  1. Visit the official Node.js website at
    [nodejs.org](https://nodejs.org/)
    .

  2. Click on the
    **LTS**
    (Long Term Support) or
    **Current**
    version download button, as per your requirement.

  3. Run the downloaded installer and follow the prompts to complete the installation.

#### How do you update Node.js?

  To update [Node.js](../N/node-js.md), you can use a package manager like `nvm` (Node Version Manager) or `n` for Unix-based systems, or download the latest version directly from the [Node.js](../N/node-js.md) website for Windows.
  **Using nvm:**

  1. Open your terminal.
  2. Run
    `nvm ls`
    to list installed versions.

  3. Update to the latest version with
    `nvm install node`
    .

  4. Switch to the new version using
    `nvm use node`
    .

  5. Verify the update with
    `node -v`
    .
  **Using n:**

  1. Open your terminal.
  2. Install
    `n`
    globally with
    `npm install -g n`
    .

  3. Update Node.js to the latest version with
    `n latest`
    .

  4. Verify the update with
    `node -v`
    .
  **For Windows:**

  1. Go to the
    [Node.js website](https://nodejs.org/)
    .

  2. Download the Windows Installer for the latest version.
  3. Run the installer and follow the prompts to update Node.js.
  4. Restart your terminal and verify the update with
    `node -v`
    .
  **Using npm (cross-platform):**
  If you have npm installed, you can update [Node.js](../N/node-js.md) to the latest stable version using the `npm` package `npm-windows-upgrade` on Windows or `npm` itself on Unix-based systems:

  ```
  npm install -g npm-windows-upgrade
  npm-windows-upgrade
  ```
  Or on Unix-based systems:

  ```
  npm cache clean -f
  npm install -g n
  n stable
  ```
  Always ensure your global npm packages and local project dependencies are compatible with the new [Node.js](../N/node-js.md) version after updating.

  1. Open your terminal.
  2. Run
    `nvm ls`
    to list installed versions.

  3. Update to the latest version with
    `nvm install node`
    .

  4. Switch to the new version using
    `nvm use node`
    .

  5. Verify the update with
    `node -v`
    .

  1. Open your terminal.
  2. Install
    `n`
    globally with
    `npm install -g n`
    .

  3. Update Node.js to the latest version with
    `n latest`
    .

  4. Verify the update with
    `node -v`
    .

  1. Go to the
    [Node.js website](https://nodejs.org/)
    .

  2. Download the Windows Installer for the latest version.
  3. Run the installer and follow the prompts to update Node.js.
  4. Restart your terminal and verify the update with
    `node -v`
    .

#### How can you debug a Node.js application?

  Debugging a [Node.js](../N/node-js.md) application can be done using several methods:
  **Built-in Debugger**: [Node.js](../N/node-js.md) comes with a built-in CLI debugger which can be started by running `node inspect yourScript.js`. You can set breakpoints, step through code, and inspect variables.
  **Chrome DevTools**: By starting your [Node.js](../N/node-js.md) application with the `--inspect` flag (e.g., `node --inspect yourScript.js`), you can connect to the Chrome DevTools for a more visual debugging experience.

  ```
  node --inspect yourScript.js
  ```
  **Visual Studio Code**: VS Code has excellent [Node.js](../N/node-js.md) debugging support. Configure a debugging session by creating a `.vscode/launch.json` file in your project and setting appropriate configurations.

  ```
  {
    "version": "0.2.0",
    "configurations": [
      {
        "type": "node",
        "request": "launch",
        "name": "Launch Program",
        "skipFiles": ["<node_internals>/**"],
        "program": "${workspaceFolder}/yourScript.js"
      }
    ]
  }
  ```
  **Logging**: Sometimes, simple `console.log()` statements can help trace the flow of execution and understand the state of variables at different points in your application.
  **Third-party Tools**: Tools like `node-inspector` or `ndb` can be installed via npm and provide additional debugging capabilities.
  **[Unit Testing](../U/unit-testing.md)**: Writing unit tests with libraries like Mocha or [Jest](../J/jest.md) can help isolate and debug specific parts of your application.
  **Profiling**: Use [Node.js](../N/node-js.md) profiling tools like `--prof` to identify performance bottlenecks.
  Remember to remove or comment out debugging code before deploying your application to production to avoid performance impacts and potential security risks.

#### What is NPM and how is it used in Node.js?

  NPM, or **Node Package Manager**, is a tool used for managing and sharing JavaScript packages in [Node.js](../N/node-js.md) projects. It provides a command-line interface (CLI) for installing, updating, and removing packages, as well as managing project dependencies.
  To use NPM, you typically start by initializing a new [Node.js](../N/node-js.md) project with `npm init`, which creates a `package.json` file. This file lists the project's dependencies and other metadata. To add a package, you use `npm install <package-name>`, which downloads the package from the NPM registry and adds it to the `node_modules` directory and the `package.json` file.
  For [test automation](../T/test-automation.md), NPM can be used to install testing frameworks and tools such as Mocha, [Jest](../J/jest.md), or [Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md). Here's an example of installing Mocha:

  ```
  npm install mocha --save-dev
  ```
  The `--save-dev` flag adds Mocha to the `devDependencies` in `package.json`, indicating that it's a development-only dependency.
  NPM also supports scripts, which can be defined in `package.json` and run with `npm run <script-name>`. For instance, you might define a [test script](../T/test-script.md) to run your automated tests:

  ```
  "scripts": {
    "test": "mocha"
  }
  ```
  Then, you can execute your tests with:

  ```
  npm test
  ```
  NPM ensures that all developers and CI/CD pipelines use the same package versions, thanks to the `package-lock.json` file, which locks down the exact package versions installed. This consistency is crucial for reliable, repeatable [test automation](../T/test-automation.md).

#### How do you create a server in Node.js?

  Creating a server in [Node.js](../N/node-js.md) typically involves using the built-in `http` module. Here's a succinct example of how to set up a basic HTTP server:

  ```
  const http = require('http');
  const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello, World!\n');
  });
  const PORT = 3000;
  server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
  ```
  In this example, `http.createServer()` is called with a request listener function, which is invoked each time the server receives a request. The `req` parameter represents the request object, while `res` is the response object. We set the status code to 200 (OK) and the content type to plain text. The response is ended with a message using `res.end()`.
  The server listens on the specified port (3000 in this case) and, once it's ready, the callback function is called, logging a message to the console.
  For [test automation](../T/test-automation.md) engineers, this basic server can serve as a starting point for mocking [APIs](../A/api.md) or creating a [test environment](../T/test-environment.md). It can be extended with routing, middleware, and more complex request handling logic as needed. Remember to handle errors and edge cases in a real-world application to ensure stability and reliability.

### Node.js Modules

#### What are modules in Node.js?

  Modules in [Node.js](../N/node-js.md) are encapsulated blocks of code that can be shared and reused across different parts of an application or even between different applications. They provide a way to organize code into separate files and namespaces, promoting modularity and [maintainability](../M/maintainability.md).
  Each module in [Node.js](../N/node-js.md) has its own context, meaning that variables and functions defined in a module are not accessible from outside unless explicitly exported. To use a module in another file, you must require it using the `require` function, which reads the module file, executes it, and then returns the module's `exports` object.
  Here's an example of how to define a simple module and export its functionality:

  ```
  // myModule.js
  const myFunction = () => {
    console.log('Function from myModule');
  };
  module.exports = myFunction;
  ```
  To use the exported function from `myModule.js` in another file:

  ```
  // app.js
  const myFunction = require('./myModule');
  myFunction(); // Outputs: Function from myModule
  ```
  [Node.js](../N/node-js.md) also has a set of **built-in modules** that provide various functionalities like file system access, HTTP networking, and more. These modules can be included in the same way as custom modules but without the need for a file path.

  ```
  const fs = require('fs'); // fs is a built-in module for file system operations
  ```
  Modules can export multiple values, such as functions, objects, or primitives, by attaching them to the `exports` object or by setting `module.exports` directly. This modular system is based on the CommonJS module pattern.

#### How do you create and use a module in Node.js?

  Creating a module in [Node.js](../N/node-js.md) involves encapsulating related code into a single file which can then be reused across your [Node.js](../N/node-js.md) application. To create a module, follow these steps:

  1. **Create a new file**
    with a
    `.js`
    extension, for example,
    `calculator.js`
    .

  2. **Write your module code**
    within this file. Define functions, objects, or any other variables that you want to make available to other files.

  ```
  // calculator.js
  function add(a, b) {
    return a + b;
  }
  function subtract(a, b) {
    return a - b;
  }
  module.exports = { add, subtract };
  ```

  1. Use
    `module.exports`
    to
    **export the module's functionalities**
    that you want to expose. This can be a function, object, class, etc.
  To use the module in another file:

  1. **Require the module**
    using
    `require()`
    function with the path to the module file.

  ```
  // app.js
  const calculator = require('./calculator');
  const sum = calculator.add(5, 10);
  const difference = calculator.subtract(10, 5);
  console.log(sum); // Outputs: 15
  console.log(difference); // Outputs: 5
  ```

  1. **Call the methods**
    or access the properties you've exported from the module.
  Remember, [Node.js](../N/node-js.md) uses the CommonJS module system, and each file is treated as a separate module. By using `require()` and `module.exports`, you can create modular, maintainable, and reusable code, which is particularly useful in [test automation](../T/test-automation.md) for structuring your [test cases](../T/test-case.md) and utility functions.

  1. **Create a new file**
    with a
    `.js`
    extension, for example,
    `calculator.js`
    .

  2. **Write your module code**
    within this file. Define functions, objects, or any other variables that you want to make available to other files.

  1. Use
    `module.exports`
    to
    **export the module's functionalities**
    that you want to expose. This can be a function, object, class, etc.

  1. **Require the module**
    using
    `require()`
    function with the path to the module file.

  1. **Call the methods**
    or access the properties you've exported from the module.

#### What are some of the built-in modules in Node.js?

  [Node.js](../N/node-js.md) comes with a variety of built-in modules that provide foundational functionality without the need for external libraries. Some of these include:

  - **fs** : Offers file system operations like reading and writing files.

    ```
    const fs = require('fs');
    ```

  - **http** : Enables the creation of HTTP servers and clients.

    ```
    const http = require('http');
    ```

  - **https** : Similar to
    `http`
    but for HTTPS.

    ```
    const https = require('https');
    ```

  - **path** : Provides utilities for handling and transforming file paths.

    ```
    const path = require('path');
    ```

  - **os** : Offers basic operating-system related utility functions.

    ```
    const os = require('os');
    ```

  - **util** : Contains utility functions for debugging and deprecation handling.

    ```
    const util = require('util');
    ```

  - **events** : Provides the EventEmitter class for handling events.

    ```
    const EventEmitter = require('events');
    ```

  - **stream** : Allows handling of streaming data, like reading and writing files in chunks.

    ```
    const stream = require('stream');
    ```

  - **child_process** : Enables running child processes for executing other programs.

    ```
    const { exec } = require('child_process');
    ```

  - **url** : Provides utilities for URL resolution and parsing.

    ```
    const url = require('url');
    ```

  - **querystring** : Parses and formats URL query strings.

    ```
    const querystring = require('querystring');
    ```

  - **crypto** : Offers cryptographic functionality including a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.

    ```
    const crypto = require('crypto');
    ```

  - **buffer** : Deals with binary data directly using the Buffer class.

    ```
    const Buffer = require('buffer').Buffer;
    ```

  - **dns** : Provides functions to perform name resolution.

    ```
    const dns = require('dns');
    ```

  - **net** : Offers asynchronous network wrappers for creating stream-based TCP or IPC servers and clients.

    ```
    const net = require('net');
    ```
  These modules are integral to [Node.js](../N/node-js.md) and can be included in your application with the `require` function. They provide the tools necessary to build complex applications with ease.

  - **fs** : Offers file system operations like reading and writing files.

    ```
    const fs = require('fs');
    ```

  - **http** : Enables the creation of HTTP servers and clients.

    ```
    const http = require('http');
    ```

  - **https** : Similar to
    `http`
    but for HTTPS.

    ```
    const https = require('https');
    ```

  - **path** : Provides utilities for handling and transforming file paths.

    ```
    const path = require('path');
    ```

  - **os** : Offers basic operating-system related utility functions.

    ```
    const os = require('os');
    ```

  - **util** : Contains utility functions for debugging and deprecation handling.

    ```
    const util = require('util');
    ```

  - **events** : Provides the EventEmitter class for handling events.

    ```
    const EventEmitter = require('events');
    ```

  - **stream** : Allows handling of streaming data, like reading and writing files in chunks.

    ```
    const stream = require('stream');
    ```

  - **child_process** : Enables running child processes for executing other programs.

    ```
    const { exec } = require('child_process');
    ```

  - **url** : Provides utilities for URL resolution and parsing.

    ```
    const url = require('url');
    ```

  - **querystring** : Parses and formats URL query strings.

    ```
    const querystring = require('querystring');
    ```

  - **crypto** : Offers cryptographic functionality including a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.

    ```
    const crypto = require('crypto');
    ```

  - **buffer** : Deals with binary data directly using the Buffer class.

    ```
    const Buffer = require('buffer').Buffer;
    ```

  - **dns** : Provides functions to perform name resolution.

    ```
    const dns = require('dns');
    ```

  - **net** : Offers asynchronous network wrappers for creating stream-based TCP or IPC servers and clients.

    ```
    const net = require('net');
    ```

#### What is the purpose of module.exports in Node.js?

  In [Node.js](../N/node-js.md), `module.exports` is an object that the current module returns when it is `require`d in another module. Essentially, it defines the **exportable entities** from a module, such as functions, objects, or primitives, making them accessible to other modules.
  Here's a basic example of how `module.exports` is used:

  ```
  // In a file named greet.js
  function sayHello(name) {
    return `Hello, ${name}!`;
  }
  module.exports = sayHello;
  ```
  In another file, you can use the exported function:

  ```
  // In another file
  const greet = require('./greet');
  console.log(greet('World')); // Outputs: Hello, World!
  ```
  `module.exports` can also export multiple entities by attaching them to the `exports` object:

  ```
  // In greet.js
  function sayHello(name) {
    return `Hello, ${name}!`;
  }
  function sayGoodbye(name) {
    return `Goodbye, ${name}!`;
  }
  module.exports = {
    sayHello,
    sayGoodbye
  };
  ```
  Then, you can destructure to use multiple exported functions:

  ```
  // In another file
  const { sayHello, sayGoodbye } = require('./greet');
  console.log(sayHello('Alice')); // Outputs: Hello, Alice!
  console.log(sayGoodbye('Bob')); // Outputs: Goodbye, Bob!
  ```
  This mechanism is crucial for creating **modular** and **maintainable** codebases, where each module exposes only the necessary parts to the rest of the application, enhancing **encapsulation** and **reusability**.

#### How do you include third-party modules in a Node.js application?

  To include third-party modules in a [Node.js](../N/node-js.md) application, use **npm** (Node Package Manager) or **yarn**, which are command-line tools for managing packages. Follow these steps:

  1. **Initialize your project** (if not already done) by running `npm init` or `yarn init`. This creates a `package.json` file that tracks your project's dependencies.
  2. **Install a third-party module** by running `npm install <module-name>` or `yarn add <module-name>`. Replace `<module-name>` with the actual name of the module you want to include. This command downloads the module and its dependencies into the `node_modules` directory and updates the `package.json` file.
  3. **Require the module** in your application code using the `require()` function. For example:
    This line imports the `express` module, which you can now use in your application.

    ```
    const express = require('express');
    ```

  4. **Save the module as a development dependency** if it's only needed for development purposes (e.g., testing frameworks) by using the `--save-dev` flag:
    or for yarn:

    ```
    npm install <module-name> --save-dev
    ```

    ```
    yarn add <module-name> --dev
    ```

  5. **Use the module** in your code by calling its functions or classes as per the module's documentation.
  Remember to **commit the `package.json` and `package-lock.json` or `yarn.lock`** files to your version control system to ensure that other developers can install the same dependencies. However, the `node_modules` directory is typically added to `.gitignore` as it can be easily reconstructed with `npm install` or `yarn install`.

  1. **Initialize your project** (if not already done) by running `npm init` or `yarn init`. This creates a `package.json` file that tracks your project's dependencies.
  2. **Install a third-party module** by running `npm install <module-name>` or `yarn add <module-name>`. Replace `<module-name>` with the actual name of the module you want to include. This command downloads the module and its dependencies into the `node_modules` directory and updates the `package.json` file.
  3. **Require the module** in your application code using the `require()` function. For example:
    This line imports the `express` module, which you can now use in your application.

    ```
    const express = require('express');
    ```

  4. **Save the module as a development dependency** if it's only needed for development purposes (e.g., testing frameworks) by using the `--save-dev` flag:
    or for yarn:

    ```
    npm install <module-name> --save-dev
    ```

    ```
    yarn add <module-name> --dev
    ```

  5. **Use the module** in your code by calling its functions or classes as per the module's documentation.

### Node.js and Databases

#### How do you connect a Node.js application to a database?

  To connect a [Node.js](../N/node-js.md) application to a [database](../D/database.md), you typically use a **[database](../D/database.md) driver** or an **ORM (Object-Relational Mapping)** library compatible with your chosen [database](../D/database.md). Here's a general process using a driver for a **MySQL** [database](../D/database.md) as an example:

  1. **Install the [database](../D/database.md) driver** using npm. For MySQL, you would run:

    ```
    npm install mysql
    ```

  2. **Import the driver** in your [Node.js](../N/node-js.md) application:

    ```
    const mysql = require('mysql');
    ```

  3. **Create a connection** to the [database](../D/database.md) with the necessary credentials:

    ```
    const connection = mysql.createConnection({
      host: 'localhost',
      user: 'your_username',
      password: 'your_password',
      database: 'your_database_name'
    });
    ```

  4. **Open the connection** and handle any errors:

    ```
    connection.connect(error => {
      if (error) throw error;
      console.log('Connected to the database.');
    });
    ```

  5. **Perform [database](../D/database.md) operations** using the connection, such as querying:

    ```
    connection.query('SELECT * FROM your_table', (error, results, fields) => {
      if (error) throw error;
      // Process results here
    });
    ```

  6. **Close the connection** when done:

    ```
    connection.end();
    ```
  For other [databases](../D/database.md) like PostgreSQL or MongoDB, you would use their respective drivers (`pg` for PostgreSQL, `mongodb` for MongoDB, etc.) and follow a similar process. If using an ORM like Sequelize, the process would involve defining models and using the ORM's methods to interact with the [database](../D/database.md). Always handle errors gracefully and ensure that connections are properly closed to avoid resource leaks.

  1. **Install the [database](../D/database.md) driver** using npm. For MySQL, you would run:

    ```
    npm install mysql
    ```

  2. **Import the driver** in your [Node.js](../N/node-js.md) application:

    ```
    const mysql = require('mysql');
    ```

  3. **Create a connection** to the [database](../D/database.md) with the necessary credentials:

    ```
    const connection = mysql.createConnection({
      host: 'localhost',
      user: 'your_username',
      password: 'your_password',
      database: 'your_database_name'
    });
    ```

  4. **Open the connection** and handle any errors:

    ```
    connection.connect(error => {
      if (error) throw error;
      console.log('Connected to the database.');
    });
    ```

  5. **Perform [database](../D/database.md) operations** using the connection, such as querying:

    ```
    connection.query('SELECT * FROM your_table', (error, results, fields) => {
      if (error) throw error;
      // Process results here
    });
    ```

  6. **Close the connection** when done:

    ```
    connection.end();
    ```

#### How do you perform CRUD operations in Node.js?

  To perform CRUD operations in [Node.js](../N/node-js.md), you typically interact with a [database](../D/database.md) using a driver or an ORM. Here's a concise example using the popular MongoDB with the Mongoose ORM:
  **Create** - To insert a new document into a collection:

  ```
  const mongoose = require('mongoose');
  const { Schema } = mongoose;
  const userSchema = new Schema({ name: String, age: Number });
  const User = mongoose.model('User', userSchema);
  const newUser = new User({ name: 'Alice', age: 30 });
  newUser.save(err => {
    if (err) return handleError(err);
    // Document saved
  });
  ```
  **Read** - To fetch documents from a collection:

  ```
  User.find({ age: { $gte: 18 } }, (err, users) => {
    if (err) return handleError(err);
    // users is an array of adult users
  });
  ```
  **Update** - To modify an existing document:

  ```
  User.updateOne({ name: 'Alice' }, { age: 31 }, err => {
    if (err) return handleError(err);
    // Document updated
  });
  ```
  **Delete** - To remove a document from a collection:

  ```
  User.deleteOne({ name: 'Alice' }, err => {
    if (err) return handleError(err);
    // Document deleted
  });
  ```
  Remember to handle errors appropriately, possibly using a `handleError` function. Also, ensure you have established a connection to the [database](../D/database.md) before performing these operations. Use `async/await` for cleaner asynchronous code, avoiding callback hell.

#### What is ORM and how is it used in Node.js?

  ORM stands for **Object-Relational Mapping**, a programming technique used to convert data between incompatible type systems in object-oriented programming languages. In the context of [Node.js](../N/node-js.md), ORM allows developers to interact with a [database](../D/database.md) using JavaScript objects instead of [SQL](../S/sql.md) queries.
  ORMs provide a high-level abstraction upon a relational [database](../D/database.md) that allows for easier manipulation of data. This means that you can write [database](../D/database.md) queries using JavaScript, which can be particularly beneficial for developers who may not be familiar with [SQL](../S/sql.md) syntax.
  Here's how ORM is typically used in [Node.js](../N/node-js.md):

  1. **Install an ORM package** : Choose an ORM like Sequelize, TypeORM, or Bookshelf, and install it using npm.

    ```
    npm install sequelize
    ```

  2. **Configure ORM with [database](../D/database.md) details** : Set up the connection to your database by providing credentials and other configuration details.

    ```
    const Sequelize = require('sequelize');
    const sequelize = new Sequelize('database', 'username', 'password', {
      host: 'localhost',
      dialect: 'mysql'
    });
    ```

  3. **Define models** : Create models that represent tables in your database, mapping object properties to table columns.

    ```
    const User = sequelize.define('user', {
      username: Sequelize.STRING,
      birthday: Sequelize.DATE
    });
    ```

  4. **Perform CRUD operations** : Use the ORM methods to create, read, update, and delete records in your database.

    ```
    User.create({
      username: 'johndoe',
      birthday: new Date(1980, 6, 20)
    });
    ```
  Using an ORM can help streamline [database](../D/database.md) interactions, reduce [SQL](../S/sql.md) boilerplate, and improve code [maintainability](../M/maintainability.md). However, it's important to be aware of potential performance overhead and the complexity that ORMs can introduce, especially for complex queries.

  1. **Install an ORM package** : Choose an ORM like Sequelize, TypeORM, or Bookshelf, and install it using npm.

    ```
    npm install sequelize
    ```

  2. **Configure ORM with [database](../D/database.md) details** : Set up the connection to your database by providing credentials and other configuration details.

    ```
    const Sequelize = require('sequelize');
    const sequelize = new Sequelize('database', 'username', 'password', {
      host: 'localhost',
      dialect: 'mysql'
    });
    ```

  3. **Define models** : Create models that represent tables in your database, mapping object properties to table columns.

    ```
    const User = sequelize.define('user', {
      username: Sequelize.STRING,
      birthday: Sequelize.DATE
    });
    ```

  4. **Perform CRUD operations** : Use the ORM methods to create, read, update, and delete records in your database.

    ```
    User.create({
      username: 'johndoe',
      birthday: new Date(1980, 6, 20)
    });
    ```

#### How do you handle database errors in Node.js?

  Handling [database](../D/database.md) errors in [Node.js](../N/node-js.md) typically involves implementing error handling mechanisms that catch and respond to issues that may arise during [database](../D/database.md) operations. Here's a succinct guide:
  **Use try-catch for synchronous code**: When working with synchronous [database](../D/database.md) operations, wrap your code in `try-catch` blocks to handle errors.

  ```
  try {
    // Synchronous database operation
  } catch (error) {
    // Handle error
  }
  ```
  **Leverage Promises and async/await for asynchronous code**: Most [Node.js](../N/node-js.md) [database](../D/database.md) libraries return promises for async operations. Use `async/await` with `try-catch` for cleaner error handling.

  ```
  async function queryDatabase() {
    try {
      const result = await database.query('SELECT * FROM table');
      // Process result
    } catch (error) {
      // Handle error
    }
  }
  ```
  **Handle promise rejections**: Always handle promise rejections using `.catch()` to prevent unhandled promise rejections.

  ```
  database.query('SELECT * FROM table')
    .then(result => {
      // Process result
    })
    .catch(error => {
      // Handle error
    });
  ```
  **Use middleware for error handling in Express**: If you're using Express, define error-handling middleware to manage [database](../D/database.md) errors.

  ```
  app.use((error, req, res, next) => {
    if (error instanceof DatabaseError) {
      res.status(500).send('Database error occurred');
    } else {
      next(error);
    }
  });
  ```
  **Log errors**: Always log errors for debugging and monitoring purposes.

  ```
  console.error('Database error:', error);
  ```
  **Graceful shutdown**: If a [database](../D/database.md) error is critical, consider shutting down the process gracefully after logging the error and sending a response to the client.
  Remember to **never expose sensitive error details** to the client, as this can be a security risk. Instead, log the detailed error and send a generic error message to the client.

### Advanced Concepts

#### What is the event loop in Node.js?

  The **event loop** is a core concept in [Node.js](../N/node-js.md), enabling its non-blocking I/O operations despite being single-threaded. It's responsible for scheduling asynchronous operations and managing their completion. When [Node.js](../N/node-js.md) starts, it initializes the event loop, which repeatedly checks the **callback queue** for any pending callbacks from completed I/O events or timers.
  Here's a simplified view of the event loop's operation:

  1. **Timers** : Checks for
    `setTimeout()`
    and
    `setInterval()`
    callbacks.

  2. **Pending Callbacks** : Executes I/O-related callbacks deferred to the next loop iteration.
  3. **Idle, Prepare** : Internal maintenance phase.
  4. **Poll** : Retrieve new I/O events; execute their callbacks.
  5. **Check** :
    `setImmediate()`
    callbacks are invoked here.

  6. **Close Callbacks** : Handle
    `close`
    events, like socket closing.
  The **poll** phase is crucial as it decides how long to wait for incoming connections, requests, etc., and whether to terminate if there are no callbacks. If scripts are scheduled with `setImmediate()`, the event loop will end the poll phase and run those scripts.
  [Node.js](../N/node-js.md) uses a **libuv** library to implement the event loop, which handles the asynchronous I/O operations. The event loop enables [Node.js](../N/node-js.md) to perform non-blocking operations by offloading tasks to the system kernel whenever possible and managing callback execution once the operation is complete or data is available.

  ```
  setImmediate(() => {
    console.log('Immediate execution');
  });
  setTimeout(() => {
    console.log('Timeout execution');
  }, 0);
  // Output order may vary depending on the performance of the process
  ```
  Understanding the event loop is crucial for optimizing [Node.js](../N/node-js.md) applications and avoiding performance issues like blocking the loop with CPU-intensive tasks.

  1. **Timers** : Checks for
    `setTimeout()`
    and
    `setInterval()`
    callbacks.

  2. **Pending Callbacks** : Executes I/O-related callbacks deferred to the next loop iteration.
  3. **Idle, Prepare** : Internal maintenance phase.
  4. **Poll** : Retrieve new I/O events; execute their callbacks.
  5. **Check** :
    `setImmediate()`
    callbacks are invoked here.

  6. **Close Callbacks** : Handle
    `close`
    events, like socket closing.

#### What is callback hell and how can you avoid it in Node.js?

  Callback hell, also known as "Pyramid of Doom," refers to the scenario where callbacks are nested within other callbacks several levels deep, making the code difficult to read and maintain. This situation often arises in [Node.js](../N/node-js.md) due to its asynchronous nature.
  To avoid callback hell:

  - **Modularize**: Break down large functions into smaller, reusable ones. This makes the code more manageable and easier to follow.
  - **Named Functions**: Instead of anonymous callbacks, use named functions. This improves readability and stack traces during debugging.
  - **Control Flow Libraries**: Utilize libraries like `async` which provide powerful functions for working with asynchronous JavaScript.
  - **Promises**: Replace callbacks with promises. They allow you to chain `.then()` and `.catch()` methods, leading to flatter code structure.
  - **Async/Await**: With the introduction of async/await in ES2017, asynchronous code can be written in a synchronous manner, further flattening the structure and improving readability.
  Here's an example of converting nested callbacks into async/await:

  ```
  // Callback hell
  fs.readdir(source, function (err, files) {
    if (err) {
      console.log('Error finding files: ' + err);
    } else {
      files.forEach(function (filename, fileIndex) {
        console.log(filename);
        // More nested callbacks...
      });
    }
  });
  // Using async/await
  async function listFiles() {
    try {
      const files = await fs.promises.readdir(source);
      files.forEach(filename => {
        console.log(filename);
        // More synchronous-looking code...
      });
    } catch (err) {
      console.log('Error finding files: ' + err);
    }
  }
  ```
  By following these practices, you can write cleaner, more maintainable [Node.js](../N/node-js.md) code and effectively avoid callback hell.

  - **Modularize**: Break down large functions into smaller, reusable ones. This makes the code more manageable and easier to follow.
  - **Named Functions**: Instead of anonymous callbacks, use named functions. This improves readability and stack traces during debugging.
  - **Control Flow Libraries**: Utilize libraries like `async` which provide powerful functions for working with asynchronous JavaScript.
  - **Promises**: Replace callbacks with promises. They allow you to chain `.then()` and `.catch()` methods, leading to flatter code structure.
  - **Async/Await**: With the introduction of async/await in ES2017, asynchronous code can be written in a synchronous manner, further flattening the structure and improving readability.

#### What are promises and async/await in Node.js?

  Promises in [Node.js](../N/node-js.md) are objects representing the eventual completion or failure of an asynchronous operation. They allow you to write cleaner, more manageable asynchronous code by avoiding deeply nested callbacks, commonly known as "callback hell."
  A Promise has three states:

  - **Pending** : Initial state, neither fulfilled nor rejected.
  - **Fulfilled** : The operation completed successfully.
  - **Rejected** : The operation failed.
  Here's a basic example of a Promise:

  ```
  const myPromise = new Promise((resolve, reject) => {
    // Asynchronous operation here
    if (/* operation successful */) {
      resolve('Success!');
    } else {
      reject('Failure.');
    }
  });
  myPromise.then((successMessage) => {
    console.log(successMessage);
  }).catch((failureMessage) => {
    console.log(failureMessage);
  });
  ```
  `async/await` is syntactic sugar built on top of Promises, introduced in ES2017, to simplify writing asynchronous code in a more synchronous fashion. The `async` keyword is added to functions to tell them to return a Promise. The `await` keyword is used to pause the execution of the function until the Promise is resolved.
  Example using `async/await`:

  ```
  async function asyncFunction() {
    try {
      const result = await someAsyncOperation();
      console.log(result);
    } catch (error) {
      console.error(error);
    }
  }
  ```
  `async/await` makes the asynchronous code look and behave a little more like synchronous code, which can make it easier to understand and maintain.

  - **Pending** : Initial state, neither fulfilled nor rejected.
  - **Fulfilled** : The operation completed successfully.
  - **Rejected** : The operation failed.

#### What is the cluster module in Node.js and why is it useful?

  The **cluster module** in [Node.js](../N/node-js.md) allows you to create child processes that all share server ports. It's useful for enabling **load balancing** over multiple CPU cores. Since [Node.js](../N/node-js.md) is single-threaded, by default, it doesn't take advantage of multi-core systems. The cluster module solves this by forking the main [Node.js](../N/node-js.md) process into multiple child processes that can run simultaneously.
  Each child process, also known as a worker, is a separate instance of the [Node.js](../N/node-js.md) event loop. This means that your [Node.js](../N/node-js.md) application can handle more tasks in parallel, improving performance and throughput. The workers are spawned using the `fork` method of the `child_process` module, and they communicate with the parent process via IPC (Inter-Process Communication).
  Here's a basic example of how to use the cluster module:

  ```
  const cluster = require('cluster');
  const http = require('http');
  const numCPUs = require('os').cpus().length;
  if (cluster.isMaster) {
    console.log(`Master ${process.pid} is running`);
    // Fork workers.
    for (let i = 0; i < numCPUs; i++) {
      cluster.fork();
    }
    cluster.on('exit', (worker, code, signal) => {
      console.log(`worker ${worker.process.pid} died`);
    });
  } else {
    // Workers can share any TCP connection
    // In this case it is an HTTP server
    http.createServer((req, res) => {
      res.writeHead(200);
      res.end('Hello world\n');
    }).listen(8000);
    console.log(`Worker ${process.pid} started`);
  }
  ```
  In testing environments, the cluster module can be particularly useful for simulating high-traffic scenarios and ensuring that the application can scale effectively across multiple processors. It's also beneficial for maximizing resource utilization during [performance testing](../P/performance-testing.md).

#### How does Node.js handle child processes?

  [Node.js](../N/node-js.md) handles child processes using the `child_process` module, which allows it to execute other applications or scripts in a new process. This module provides various ways to spawn child processes, such as `exec`, `execFile`, `spawn`, and `fork`.

  - **exec** : Used for running a command in a shell and buffering the output. Suitable for small-sized data as it buffers the output in memory.

  ```
  const { exec } = require('child_process');
  exec('ls -lh', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
  });
  ```

  - **execFile** : Similar to
    `exec`
    but does not spawn a shell by default. It's more efficient for calling executable files.

  ```
  const { execFile } = require('child_process');
  execFile('script.sh', (error, stdout, stderr) => {
    // handle output
  });
  ```

  - **spawn** : Launches a new process with a given command. It streams data in/out, making it suitable for large data volumes.

  ```
  const { spawn } = require('child_process');
  const child = spawn('ls', ['-lh', '/usr']);
  child.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });
  ```

  - **fork** : A special case of
    `spawn`
    that creates a new instance of the V8 engine. It's used for running Node.js modules in separate processes and enables inter-process communication (IPC).

  ```
  const { fork } = require('child_process');
  const child = fork('script.js');
  child.on('message', (message) => {
    console.log('Message from child', message);
  });
  child.send({ hello: 'world' });
  ```
  Child processes are useful for performing CPU-intensive operations without blocking the [Node.js](../N/node-js.md) event loop, thus maintaining the application's responsiveness.

  - **exec** : Used for running a command in a shell and buffering the output. Suitable for small-sized data as it buffers the output in memory.
  - **execFile** : Similar to
    `exec`
    but does not spawn a shell by default. It's more efficient for calling executable files.

  - **spawn** : Launches a new process with a given command. It streams data in/out, making it suitable for large data volumes.
  - **fork** : A special case of
    `spawn`
    that creates a new instance of the V8 engine. It's used for running Node.js modules in separate processes and enables inter-process communication (IPC).
