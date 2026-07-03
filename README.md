# fleet-sandbox
Throwaway target repo for AgentOS fleet build→PR proof (safe to delete)

## sb_smoke2 Usage Example

To test the ping2 function from sb_smoke2:

```python
import sys
sys.path.insert(0, '.')
from sb_smoke2 import ping2
assert ping2() == 'pong2'
```