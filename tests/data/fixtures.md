Empty expression
.

```nix
{}
```

.

```nix
{}
```

.

Expression with multiple properties
.

```nix
{foo=42;
bar="Hello, world!";baz=true;}
```

.

```nix
{
  foo = 42;
  bar = "Hello, world!";
  baz = true;
}
```

.

Commented expression
.

```nix
{ # This is a comment
  foo = 42;
}
```

.

```nix
{
  # This is a comment
  foo = 42;
}
```

.

Commented expression with specifics for mkdocs
.

```nix
{
  foo = 42; # 1 This is a comment
}
```

.

```nix
{
  foo = 42; # 1 This is a comment
}
```

.
