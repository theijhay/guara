# Asynchronous execution
As describe in [main page](https://github.com/douglasdcm/guara?tab=readme-ov-file#introduction)

> [!IMPORTANT]
> Guará is the Python implementation of the desing pattern `Page Transactions`. It is more of a programming pattern than a tool. It can be bound to any web driver other than Selenium.

As it can be bound to any Web Driver it can be associated with asynchronous drivers like [Caqui](https://github.com/douglasdcm/caqui). The core of the framework was extended to allow it. The UML diagrams of the asynchornous classes are

<p align="center">
    <img src="https://github.com/douglasdcm/guara/blob/main/guara/asynchronous/uml_abstract_transaction.png?raw=true" width="800" height="300" />
</p>

Notice the introduction of the `perform` method. It is necessary to run the chain of built-in methods `at` and `assert`. It calls the list of coroutines. If it is not executed, the built-in methods are not `waited`.

<p align="center">
    <img src="https://github.com/douglasdcm/guara/blob/main/guara/asynchronous/uml_abstract_transaction.png?raw=true" width="800" height="300" />
</p>

The built-in classes `OpenApp` and `CloseApp` are here just for compatibility with the synchronous design, but it is not implemented and not bound to any driver. Testers need to choose it by themselves.

<p align="center">
    <img src="https://github.com/douglasdcm/guara/blob/main/guara/asynchronous/uml_iassertion.png?raw=true" width="800" height="300" />
</p>

There is a subtle change in `asserts` method. In this design the `actual` is an `AbstractTransaction`. Internally the method gets the `AbstractTransaction.result` and compares it against the expected value.

# Examples

Check more details [here](https://github.com/douglasdcm/guara/blob/main/tests/web_ui_async/asynchronouos/test_async.py) 