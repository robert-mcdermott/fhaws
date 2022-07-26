# FHAWS

Helper functions to make working with Boto3 easier
## Organizations

A collections of functions for AWS Organizations

```python
import fhaws.org as org
```

**Available Functions**

### **getaccounts(profile)**


Returns a dictionary of all AWS accounts that are members of the organization.

Required parameters:

1. profile:  the name of the AWS profile to use


### **account_inventory(profile)**

Returns a CSV report, including all available information on all AWS accounts that are members of the AWS Organization.

Required parameters:

1. profile:  the name of the AWS profile to use

Provided fields:

- Name
- Id
- Email
- Arn
- Status
- JoinedMethod
- JoinedTimestamp


### **getorg(profile)**

Get information about the organization 

Required parameters:

1. profile:  the name of the AWS profile to use

### **getroots(profile)**

Get information about the root of the organization

Required parameters:

1. profile:  the name of the AWS profile to use

### **getous(profile, parent)**

Get the OUs directly under the specified parent (root or parent OU)

Required parameters:

1. profile: the name of the AWS profile to use
2. parent: the id of the parent object

### **getchildren(profile, parent, child_type)**

Get the children objects under the parent. you must also specify the type of children you want "

Required parameters:

1. profile: the name of the AWS profile to use
2. parent: the id of the parent object
3. child_type: the type of child objects you want ('ACCOUNT' or 'ORGANIZATIONAL_UNIT')

