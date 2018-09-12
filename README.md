# Shelly

Compiles Lisp to [Shell Command Language](http://pubs.opengroup.org/onlinepubs/009695399/utilities/xcu_chap02.html)

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
