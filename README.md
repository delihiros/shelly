# Shelly

Compiles Lisp to shell script

```
(function param1 param2)
function param1 param2

(if (= str1 str2) a b)
if [ $str1 = $str2 ]; then
  a
else
  b
fi
```

tested with Python 3.6