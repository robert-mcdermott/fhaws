# FHAWS

Helper functions to make working with Boto3 and AWS easier via Python
## Organizations

![Example Organization Diagram](/images/example-org-diagram-1.png)

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

### **account_name_lookup(profile)**

Generate a account Id to Name lookup dictionary

Required parameters:

1. profile: the name of the AWS profile to use

### **org_structure(profile)**

Generate an dictionary containing the structure of the organization. OUs are Keys with a list of the children accounts as the value.

Required parameters:

1. profile: the name of the AWS profile to use

### **org_diagram(profile)**

Generate a mermaid formatted diagram of the organizational structure, similar to the example diagram at the top of the Organziations section above.

Required parameters:

1. profile: the name of the AWS profile to use

## IAM

A collection for working with AWS IAM 

```python
import fhaws.iam as iam
```

### **get_users(profile)**

Get all IAM user objects in the AWS account


### **inventory_users(profile)**

Get a CSV inventory of all IAM users in the AWS account
