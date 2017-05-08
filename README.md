# Cargo API
This API works with html parse. You do not have to any api key for use cargo api.

# Companies
- Yurtiçi Kargo
- Aras Kargo
- UPS

# Run
```python
import cargo_api
from cargo_api import *

c_api = cargo_api()
result = c_api.yurtici('3121768*****')
#result:boolean
```

# Output
If cargo arrived a person, return true.
