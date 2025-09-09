def say_hello():
    hello = "hello"
    print(hello)
    return hello


def get_version():
    """Return the package version."""
    try:
        from importlib.metadata import version
        return version("MyHelloWorldProject")
    except Exception:
        # Fallback if package not installed
        return "0.0.1"
