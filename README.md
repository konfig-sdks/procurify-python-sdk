<div align="left">

[![Visit Procurify](./header.png)](https://www.procurify.com&#x2F;)

# Procurify<a id="procurify"></a>


# Disclaimer<a id="disclaimer"></a>

- Procurify’s API is evolving and is subject to change at any time. Additionally, aspects of the API are undocumented, including certain methods, events, and properties. Given that both documented and undocumented aspects of the Procurify API may change at any time, the client relies on the API at their own risk.
- Client (and/or client’s representative) is responsible for building, testing, and maintaining any API connection between Procurify and any other tool.  Procurify’s responsibility strictly involves providing support on clarifications in regards to the issued API document.
- Procurify’s API is offered on an “as is” and “as available” basis, without warranties of any kind. By accepting this agreement, you agree that you have read the current API documentation, and accept the API functionality in its current state including current limitations. For questions and clarification around the documentation, please contact support@procurify.com.
- In accordance with Section 2.(b) of our Subscription Services Agreement, Procurify reserves the right to deny access to our API at any time. If your API requests are too large and time out, contact us immediately to avoid possible suspension of access.
- You may not attempt to reverse engineer or otherwise derive source code, trade secrets, or know-how in the Procurify API or portion thereof. You may not use the Procurify API to replicate or compete with core products or services offered by Procurify.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`procurify.account_codes.create_account_codes`](#procurifyaccount_codescreate_account_codes)
  * [`procurify.account_codes.list`](#procurifyaccount_codeslist)
  * [`procurify.account_codes.update_account_code`](#procurifyaccount_codesupdate_account_code)
  * [`procurify.accounts.list`](#procurifyaccountslist)
  * [`procurify.ap.bills_get_by_id`](#procurifyapbills_get_by_id)
  * [`procurify.ap.bills_list`](#procurifyapbills_list)
  * [`procurify.ap.company_payment_methods_list`](#procurifyapcompany_payment_methods_list)
  * [`procurify.ap.create_company_payment_method`](#procurifyapcreate_company_payment_method)
  * [`procurify.ap.create_vendor_payment_method`](#procurifyapcreate_vendor_payment_method)
  * [`procurify.ap.get_payments`](#procurifyapget_payments)
  * [`procurify.ap.items_get`](#procurifyapitems_get)
  * [`procurify.ap.payments_approver_choices_retrieve`](#procurifyappayments_approver_choices_retrieve)
  * [`procurify.ap.vendor_payment_methods_list`](#procurifyapvendor_payment_methods_list)
  * [`procurify.catalog.get_all_bundles`](#procurifycatalogget_all_bundles)
  * [`procurify.catalog.get_all_items`](#procurifycatalogget_all_items)
  * [`procurify.catalog.item_create`](#procurifycatalogitem_create)
  * [`procurify.catalog.update_item`](#procurifycatalogupdate_item)
  * [`procurify.currencies.list`](#procurifycurrencieslist)
  * [`procurify.custom_fields.get_order_item_custom_fields`](#procurifycustom_fieldsget_order_item_custom_fields)
  * [`procurify.custom_fields.update_order_item_custom_field_dropdown_choices`](#procurifycustom_fieldsupdate_order_item_custom_field_dropdown_choices)
  * [`procurify.departments.create`](#procurifydepartmentscreate)
  * [`procurify.departments.list`](#procurifydepartmentslist)
  * [`procurify.departments.update`](#procurifydepartmentsupdate)
  * [`procurify.locations.create`](#procurifylocationscreate)
  * [`procurify.locations.list`](#procurifylocationslist)
  * [`procurify.locations.retrieve`](#procurifylocationsretrieve)
  * [`procurify.oauth.token_request`](#procurifyoauthtoken_request)
  * [`procurify.order_items.list_items`](#procurifyorder_itemslist_items)
  * [`procurify.permissions.get_available_system_roles`](#procurifypermissionsget_available_system_roles)
  * [`procurify.permissions.list`](#procurifypermissionslist)
  * [`procurify.purchase_orders.close_order`](#procurifypurchase_ordersclose_order)
  * [`procurify.purchase_orders.get_by_id_with_items`](#procurifypurchase_ordersget_by_id_with_items)
  * [`procurify.purchase_orders.get_by_role_and_status`](#procurifypurchase_ordersget_by_role_and_status)
  * [`procurify.purchase_orders.reopen_procurify_po`](#procurifypurchase_ordersreopen_procurify_po)
  * [`procurify.purchase_orders.revise_procurify_po`](#procurifypurchase_ordersrevise_procurify_po)
  * [`procurify.purchase_orders.update_order`](#procurifypurchase_ordersupdate_order)
  * [`procurify.purchase_orders.view_billing_history`](#procurifypurchase_ordersview_billing_history)
  * [`procurify.requisitions.create`](#procurifyrequisitionscreate)
  * [`procurify.requisitions.get_all_order_items`](#procurifyrequisitionsget_all_order_items)
  * [`procurify.requisitions.get_all_orders`](#procurifyrequisitionsget_all_orders)
  * [`procurify.users.create`](#procurifyuserscreate)
  * [`procurify.users.destroy`](#procurifyusersdestroy)
  * [`procurify.users.get_logged_in_user`](#procurifyusersget_logged_in_user)
  * [`procurify.users.list`](#procurifyuserslist)
  * [`procurify.users.update`](#procurifyusersupdate)
  * [`procurify.vendors.create`](#procurifyvendorscreate)
  * [`procurify.vendors.list`](#procurifyvendorslist)
  * [`procurify.vendors.partial_update`](#procurifyvendorspartial_update)
  * [`procurify.vendors.retrieve`](#procurifyvendorsretrieve)
  * [`procurify.vendors.update`](#procurifyvendorsupdate)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Procurify&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from procurify_python_sdk import Procurify, ApiException

procurify = Procurify(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD',

    access_token = 'YOUR_BEARER_TOKEN',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

        cookie_auth = 'YOUR_API_KEY',

        token_auth = 'YOUR_API_KEY',
)

try:
    # Create Account Codes
    create_account_codes_response = procurify.account_codes.create_account_codes(
        description="a",
        code="a",
        parent=1,
        account_type=0,
        departments=[
        1
    ],
        format="csv",
    )
    print(create_account_codes_response)
except ApiException as e:
    print("Exception when calling AccountCodesApi.create_account_codes: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from procurify_python_sdk import Procurify, ApiException

procurify = Procurify(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD',

    access_token = 'YOUR_BEARER_TOKEN',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

        cookie_auth = 'YOUR_API_KEY',

        token_auth = 'YOUR_API_KEY',
)

async def main():
    try:
        # Create Account Codes
        create_account_codes_response = await procurify.account_codes.acreate_account_codes(
            description="a",
            code="a",
            parent=1,
            account_type=0,
            departments=[
        1
    ],
            format="csv",
        )
        print(create_account_codes_response)
    except ApiException as e:
        print("Exception when calling AccountCodesApi.create_account_codes: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from procurify_python_sdk import Procurify, ApiException

procurify = Procurify(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD',

    access_token = 'YOUR_BEARER_TOKEN',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

        cookie_auth = 'YOUR_API_KEY',

        token_auth = 'YOUR_API_KEY',
)

try:
    # Create Account Codes
    create_account_codes_response = procurify.account_codes.raw.create_account_codes(
        description="a",
        code="a",
        parent=1,
        account_type=0,
        departments=[
        1
    ],
        format="csv",
    )
    pprint(create_account_codes_response.body)
    pprint(create_account_codes_response.body["data"])
    pprint(create_account_codes_response.body["metadata"])
    pprint(create_account_codes_response.headers)
    pprint(create_account_codes_response.status)
    pprint(create_account_codes_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountCodesApi.create_account_codes: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `procurify.account_codes.create_account_codes`<a id="procurifyaccount_codescreate_account_codes"></a>

**Account Code Types**

| Account Code Type | Type |
|-------------------|------|
| ASSETS            | 0    |
| LIABILITY         | 1    |
| EXPENSE           | 2    |
| INCOME            | 3    |
| EQUITY            | 4    |
| OTHER             | 5    |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_account_codes_response = procurify.account_codes.create_account_codes(
    description="a",
    code="a",
    parent=1,
    account_type=0,
    departments=[
        1
    ],
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

##### code: `str`<a id="code-str"></a>

##### parent: `Optional[int]`<a id="parent-optionalint"></a>

##### account_type: [`ExpenseTypeEnum`](./procurify_python_sdk/type/expense_type_enum.py)<a id="account_type-expensetypeenumprocurify_python_sdktypeexpense_type_enumpy"></a>

##### departments: [`AccountCodeCreateRequestDepartments`](./procurify_python_sdk/type/account_code_create_request_departments.py)<a id="departments-accountcodecreaterequestdepartmentsprocurify_python_sdktypeaccount_code_create_request_departmentspy"></a>

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCodeCreateRequest`](./procurify_python_sdk/type/account_code_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccountCodeReadSerializerSingleCreate`](./procurify_python_sdk/pydantic/account_code_read_serializer_single_create.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/account-codes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.account_codes.list`<a id="procurifyaccount_codeslist"></a>

**Account Code Types**

| Account Code Type | Type |
|-------------------|------|
| ASSETS            | 0    |
| LIABILITY         | 1    |
| EXPENSE           | 2    |
| INCOME            | 3    |
| EQUITY            | 4    |
| OTHER             | 5    |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = procurify.account_codes.list(
    active=True,
    code="string_example",
    format="csv",
    is_parent=True,
    order_by="string_example",
    page=1,
    page_size=1,
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### active: `bool`<a id="active-bool"></a>

##### code: `str`<a id="code-str"></a>

##### format: `str`<a id="format-str"></a>

##### is_parent: `bool`<a id="is_parent-bool"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### search: `str`<a id="search-str"></a>

A search term.

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedAccountCodeReadList`](./procurify_python_sdk/pydantic/paginated_account_code_read_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/account-codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.account_codes.update_account_code`<a id="procurifyaccount_codesupdate_account_code"></a>

**Account Code Types**

| Account Code Type | Type |
|-------------------|------|
| ASSETS            | 0    |
| LIABILITY         | 1    |
| EXPENSE           | 2    |
| INCOME            | 3    |
| EQUITY            | 4    |
| OTHER             | 5    |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_account_code_response = procurify.account_codes.update_account_code(
    description="a",
    code="a",
    id=1,
    account_type=0,
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

##### code: `str`<a id="code-str"></a>

##### id: `int`<a id="id-int"></a>

A unique integer value identifying this account code.

##### account_type: [`ExpenseTypeEnum`](./procurify_python_sdk/type/expense_type_enum.py)<a id="account_type-expensetypeenumprocurify_python_sdktypeexpense_type_enumpy"></a>

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCodeUpdateRequest`](./procurify_python_sdk/type/account_code_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccountCodeReadSerializerSingleUpdate`](./procurify_python_sdk/pydantic/account_code_read_serializer_single_update.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/account-codes/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.accounts.list`<a id="procurifyaccountslist"></a>

Get Accounts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = procurify.accounts.list(
    account_code=1,
    active=True,
    department=1,
    departments="string_example",
    format="csv",
    id=1,
    in_effect=True,
    locations="string_example",
    order_by="string_example",
    page=1,
    page_size=1,
    search="string_example",
    with_expired_budgets=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_code: `int`<a id="account_code-int"></a>

##### active: `bool`<a id="active-bool"></a>

##### department: `int`<a id="department-int"></a>

##### departments: `str`<a id="departments-str"></a>

A comma-separated list of integers.

##### format: `str`<a id="format-str"></a>

##### id: `int`<a id="id-int"></a>

##### in_effect: `bool`<a id="in_effect-bool"></a>

##### locations: `str`<a id="locations-str"></a>

A comma-separated list of integers.

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### search: `str`<a id="search-str"></a>

A search term.

##### with_expired_budgets: `bool`<a id="with_expired_budgets-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedChartOfAccountsAccountList`](./procurify_python_sdk/pydantic/paginated_chart_of_accounts_account_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.ap.bills_get_by_id`<a id="procurifyapbills_get_by_id"></a>

 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bills_get_by_id_response = procurify.ap.bills_get_by_id(
    id="f",
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### format: `str`<a id="format-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BillMetadataBillRead`](./procurify_python_sdk/pydantic/bill_metadata_bill_read.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/ap/bills/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.ap.bills_list`<a id="procurifyapbills_list"></a>

list:
This endpoint supports OPTIONS method which returns a list of available fields and their types.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bills_list_response = procurify.ap.bills_list(
    approver=3.14,
    contract=3.14,
    currency=1,
    due_date_0="1970-01-01",
    due_date_1="1970-01-01",
    exclude_bill_group_ids="string_example",
    exclude_expense_bills="string_example",
    expense="string_example",
    format="csv",
    gl_post_date_0="1970-01-01",
    gl_post_date_1="1970-01-01",
    group=1,
    has_payment=True,
    has_posting_date=True,
    include_bill_group_ids="string_example",
    invoice_date_0="1970-01-01",
    invoice_date_1="1970-01-01",
    is_exported=True,
    last_export_date_0="1970-01-01",
    last_export_date_1="1970-01-01",
    last_export_user=3.14,
    last_modified_datetime_0="1970-01-01T00:00:00.00Z",
    last_modified_datetime_1="1970-01-01T00:00:00.00Z",
    modified_date_0="1970-01-01",
    modified_date_1="1970-01-01",
    order_by="string_example",
    page=1,
    page_size=1,
    search="string_example",
    submitted_date_0="1970-01-01",
    submitted_date_1="1970-01-01",
    sync_status="string_example",
    sync_status_v2="string_example",
    type=0,
    user=1,
    vendor=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### approver: `Union[int, float]`<a id="approver-unionint-float"></a>

Approver

##### contract: `Union[int, float]`<a id="contract-unionint-float"></a>

Contracts related to bill items' purchase orders

##### currency: `int`<a id="currency-int"></a>

##### due_date_0: `date`<a id="due_date_0-date"></a>

Due Date

##### due_date_1: `date`<a id="due_date_1-date"></a>

Due Date

##### exclude_bill_group_ids: `str`<a id="exclude_bill_group_ids-str"></a>

##### exclude_expense_bills: `str`<a id="exclude_expense_bills-str"></a>

Exclude expense bills

##### expense: `str`<a id="expense-str"></a>

Expense Bills Only

##### format: `str`<a id="format-str"></a>

##### gl_post_date_0: `date`<a id="gl_post_date_0-date"></a>

Posting Date

##### gl_post_date_1: `date`<a id="gl_post_date_1-date"></a>

Posting Date

##### group: `int`<a id="group-int"></a>

##### has_payment: `bool`<a id="has_payment-bool"></a>

Without Payment

##### has_posting_date: `bool`<a id="has_posting_date-bool"></a>

Has Posting Date

##### include_bill_group_ids: `str`<a id="include_bill_group_ids-str"></a>

##### invoice_date_0: `date`<a id="invoice_date_0-date"></a>

Invoice Date

##### invoice_date_1: `date`<a id="invoice_date_1-date"></a>

Invoice Date

##### is_exported: `bool`<a id="is_exported-bool"></a>

Exported Bills Only

##### last_export_date_0: `date`<a id="last_export_date_0-date"></a>

Last Export Date

##### last_export_date_1: `date`<a id="last_export_date_1-date"></a>

Last Export Date

##### last_export_user: `Union[int, float]`<a id="last_export_user-unionint-float"></a>

Last Export User

##### last_modified_datetime_0: `datetime`<a id="last_modified_datetime_0-datetime"></a>

Last Modified Datetime

##### last_modified_datetime_1: `datetime`<a id="last_modified_datetime_1-datetime"></a>

Last Modified Datetime

##### modified_date_0: `date`<a id="modified_date_0-date"></a>

Last Modified Date (Deprecated - use 'Last Modified Datetime')

##### modified_date_1: `date`<a id="modified_date_1-date"></a>

Last Modified Date (Deprecated - use 'Last Modified Datetime')

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### search: `str`<a id="search-str"></a>

A search term.

##### submitted_date_0: `date`<a id="submitted_date_0-date"></a>

Submitted Date

##### submitted_date_1: `date`<a id="submitted_date_1-date"></a>

Submitted Date

##### sync_status: `str`<a id="sync_status-str"></a>

Sync Status

##### sync_status_v2: `str`<a id="sync_status_v2-str"></a>

Sync Status

##### type: `int`<a id="type-int"></a>

##### user: `int`<a id="user-int"></a>

##### vendor: `int`<a id="vendor-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BillMetadataListSimpleBill`](./procurify_python_sdk/pydantic/bill_metadata_list_simple_bill.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/ap/bills` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.ap.company_payment_methods_list`<a id="procurifyapcompany_payment_methods_list"></a>

**Payment Method Types:**

| Payment Method | Type      |
|----------------|-----------|
| OTHER          | 0         |
| CHECK          | 1         |
| CHEQUE         | 1         |
| ACH            | 2         |
| EFT            | 3         |
| WIRE           | 4         |

**The context of 'data' field varies based on different Payment Method type:**

| Payment Method | 'data' field structure |
|----------------|------------------------|
| OTHER          | ```{"description": <string>}``` |
| CHECK/CHEQUE   | ```{"payable_to": <string>}```  |
| ACH            | ```{"routing_number": <string>, "account_number": <string>, "company_name": <string>}``` |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
company_payment_methods_list_response = procurify.ap.company_payment_methods_list(
    currency=1,
    format="csv",
    order_by="string_example",
    page=1,
    page_size=1,
    search="string_example",
    type=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `int`<a id="currency-int"></a>

##### format: `str`<a id="format-str"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### search: `str`<a id="search-str"></a>

A search term.

##### type: `int`<a id="type-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedCompanyPaymentMethodReadList`](./procurify_python_sdk/pydantic/paginated_company_payment_method_read_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/ap/company-payment-methods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.ap.create_company_payment_method`<a id="procurifyapcreate_company_payment_method"></a>

**Payment Method Types:**

| Payment Method | Type      |
|----------------|-----------|
| OTHER          | 0         |
| CHECK          | 1         |
| CHEQUE         | 1         |
| ACH            | 2         |
| EFT            | 3         |
| WIRE           | 4         |

**The context of 'data' field varies based on different Payment Method type:**

| Payment Method | 'data' field structure |
|----------------|------------------------|
| OTHER          | ```{"description": <string>}``` |
| CHECK/CHEQUE   | ```{"payable_to": <string>}```  |
| ACH            | ```{"routing_number": <string>, "account_number": <string>, "company_name": <string>}``` |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_company_payment_method_response = procurify.ap.create_company_payment_method(
    data={
        "key": None,
    },
    name="string_example",
    type=0,
    currency=1,
    gl_code="string_example",
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`CompanyPaymentMethodRequestData`](./procurify_python_sdk/type/company_payment_method_request_data.py)<a id="data-companypaymentmethodrequestdataprocurify_python_sdktypecompany_payment_method_request_datapy"></a>

##### name: `str`<a id="name-str"></a>

##### type: [`PaymentMethodTypeEnum`](./procurify_python_sdk/type/payment_method_type_enum.py)<a id="type-paymentmethodtypeenumprocurify_python_sdktypepayment_method_type_enumpy"></a>

##### currency: `int`<a id="currency-int"></a>

##### gl_code: `str`<a id="gl_code-str"></a>

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompanyPaymentMethodRequest`](./procurify_python_sdk/type/company_payment_method_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyPaymentMethod`](./procurify_python_sdk/pydantic/company_payment_method.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/ap/company-payment-methods` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.ap.create_vendor_payment_method`<a id="procurifyapcreate_vendor_payment_method"></a>

**Payment Method Types:**

| Payment Method | Type      |
|----------------|-----------|
| OTHER          | 0         |
| CHECK          | 1         |
| CHEQUE         | 1         |
| ACH            | 2         |
| EFT            | 3         |
| WIRE           | 4         |

**The context of 'data' field varies based on different Payment Method type:**

| Payment Method | 'data' field structure |
|----------------|------------------------|
| OTHER          | ```{"description": <string>}``` |
| CHECK/CHEQUE   | ```{"payable_to": <string>}```  |
| ACH            | ```{"routing_number": <string>, "account_number": <string>, "company_name": <string>}``` |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_vendor_payment_method_response = procurify.ap.create_vendor_payment_method(
    vendor=1,
    data={
        "key": None,
    },
    name="string_example",
    type=0,
    currency=1,
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### vendor: `int`<a id="vendor-int"></a>

##### data: [`VendorPaymentMethodRequestData`](./procurify_python_sdk/type/vendor_payment_method_request_data.py)<a id="data-vendorpaymentmethodrequestdataprocurify_python_sdktypevendor_payment_method_request_datapy"></a>

##### name: `str`<a id="name-str"></a>

##### type: [`PaymentMethodTypeEnum`](./procurify_python_sdk/type/payment_method_type_enum.py)<a id="type-paymentmethodtypeenumprocurify_python_sdktypepayment_method_type_enumpy"></a>

##### currency: `int`<a id="currency-int"></a>

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VendorPaymentMethodRequest`](./procurify_python_sdk/type/vendor_payment_method_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VendorPaymentMethod`](./procurify_python_sdk/pydantic/vendor_payment_method.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/ap/vendor-payment-methods` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.ap.get_payments`<a id="procurifyapget_payments"></a>

Get Payments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_payments_response = procurify.ap.get_payments(
    approver="string_example",
    currency=1,
    format="csv",
    order_by="string_example",
    page=1,
    page_size=1,
    payment_date_0="1970-01-01",
    payment_date_1="1970-01-01",
    payment_method__type=0,
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### approver: `str`<a id="approver-str"></a>

##### currency: `int`<a id="currency-int"></a>

##### format: `str`<a id="format-str"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### payment_date_0: `date`<a id="payment_date_0-date"></a>

##### payment_date_1: `date`<a id="payment_date_1-date"></a>

##### payment_method__type: `int`<a id="payment_method__type-int"></a>

##### search: `str`<a id="search-str"></a>

A search term.

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentMetadataPaymentListRead`](./procurify_python_sdk/pydantic/payment_metadata_payment_list_read.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/ap/payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.ap.items_get`<a id="procurifyapitems_get"></a>

 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
items_get_response = procurify.ap.items_get(
    bill=1,
    bill_uuid="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    billed=True,
    budget=1,
    created_at_0="1970-01-01",
    created_at_1="1970-01-01",
    department=3.14,
    exclude="string_example",
    format="csv",
    location=3.14,
    order_by="string_example",
    page=1,
    page_size=1,
    received_on_0="1970-01-01",
    received_on_1="1970-01-01",
    reimburse=True,
    requester=3.14,
    search="string_example",
    vendor=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bill: `int`<a id="bill-int"></a>

##### bill_uuid: `str`<a id="bill_uuid-str"></a>

##### billed: `bool`<a id="billed-bool"></a>

##### budget: `int`<a id="budget-int"></a>

##### created_at_0: `date`<a id="created_at_0-date"></a>

##### created_at_1: `date`<a id="created_at_1-date"></a>

##### department: `Union[int, float]`<a id="department-unionint-float"></a>

##### exclude: `str`<a id="exclude-str"></a>

##### format: `str`<a id="format-str"></a>

##### location: `Union[int, float]`<a id="location-unionint-float"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### received_on_0: `date`<a id="received_on_0-date"></a>

##### received_on_1: `date`<a id="received_on_1-date"></a>

##### reimburse: `bool`<a id="reimburse-bool"></a>

##### requester: `Union[int, float]`<a id="requester-unionint-float"></a>

##### search: `str`<a id="search-str"></a>

A search term.

##### vendor: `int`<a id="vendor-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ItemMetadataItemRead`](./procurify_python_sdk/pydantic/item_metadata_item_read.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/ap/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.ap.payments_approver_choices_retrieve`<a id="procurifyappayments_approver_choices_retrieve"></a>

Get Approver Choices

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
payments_approver_choices_retrieve_response = procurify.ap.payments_approver_choices_retrieve(
    id=1,
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

A unique integer value identifying this payment.

##### format: `str`<a id="format-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApproverChoicesMetadataApproverReadDocs`](./procurify_python_sdk/pydantic/approver_choices_metadata_approver_read_docs.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/ap/payments/{id}/approver-choices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.ap.vendor_payment_methods_list`<a id="procurifyapvendor_payment_methods_list"></a>

**Payment Method Types:**

| Payment Method | Type      |
|----------------|-----------|
| OTHER          | 0         |
| CHECK          | 1         |
| CHEQUE         | 1         |
| ACH            | 2         |
| EFT            | 3         |
| WIRE           | 4         |

**The context of 'data' field varies based on different Payment Method type:**

| Payment Method | 'data' field structure |
|----------------|------------------------|
| OTHER          | ```{"description": <string>}``` |
| CHECK/CHEQUE   | ```{"payable_to": <string>}```  |
| ACH            | ```{"routing_number": <string>, "account_number": <string>, "company_name": <string>}``` |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
vendor_payment_methods_list_response = procurify.ap.vendor_payment_methods_list(
    currency=1,
    format="csv",
    order_by="string_example",
    page=1,
    page_size=1,
    search="string_example",
    type=0,
    vendor=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `int`<a id="currency-int"></a>

##### format: `str`<a id="format-str"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### search: `str`<a id="search-str"></a>

A search term.

##### type: `int`<a id="type-int"></a>

##### vendor: `int`<a id="vendor-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedVendorPaymentMethodReadList`](./procurify_python_sdk/pydantic/paginated_vendor_payment_method_read_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/ap/vendor-payment-methods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.catalog.get_all_bundles`<a id="procurifycatalogget_all_bundles"></a>

Get All Catalog Bundles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_bundles_response = procurify.catalog.get_all_bundles(
    format="csv",
    order_by="string_example",
    page=1,
    page_size=1,
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### format: `str`<a id="format-str"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### search: `str`<a id="search-str"></a>

A search term.

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedCatalogItemBundleReadList`](./procurify_python_sdk/pydantic/paginated_catalog_item_bundle_read_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/catalog-bundles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.catalog.get_all_items`<a id="procurifycatalogget_all_items"></a>

Get All Catalog Items

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_items_response = procurify.catalog.get_all_items(
    bundle=1,
    department="string_example",
    format="csv",
    internal_sku="string_example",
    location="string_example",
    max_price=3.14,
    min_price=3.14,
    order_by="string_example",
    page=1,
    page_size=1,
    pref_vendor=1,
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bundle: `int`<a id="bundle-int"></a>

##### department: `str`<a id="department-str"></a>

A comma-separated list of integers.

##### format: `str`<a id="format-str"></a>

##### internal_sku: `str`<a id="internal_sku-str"></a>

##### location: `str`<a id="location-str"></a>

A comma-separated list of integers.

##### max_price: `Union[int, float]`<a id="max_price-unionint-float"></a>

##### min_price: `Union[int, float]`<a id="min_price-unionint-float"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### pref_vendor: `int`<a id="pref_vendor-int"></a>

##### search: `str`<a id="search-str"></a>

A search term.

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedCatalogItemReadList`](./procurify_python_sdk/pydantic/paginated_catalog_item_read_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/catalog-items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.catalog.item_create`<a id="procurifycatalogitem_create"></a>

Create Catalog Item

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
item_create_response = procurify.catalog.item_create(
    name="a",
    currency=1,
    custom_fields=[
        {
            "key": None,
        }
    ],
    description="string_example",
    id=1,
    image="string_example",
    unit_type="string_example",
    pref_vendor=1,
    account_code=1,
    internal_sku="string_example",
    product_url="string_example",
    price="480728",
    rfo_lock=True,
    departments=[
        1
    ],
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### currency: `int`<a id="currency-int"></a>

##### custom_fields: [`CatalogItemUpsertRequestCustomFields`](./procurify_python_sdk/type/catalog_item_upsert_request_custom_fields.py)<a id="custom_fields-catalogitemupsertrequestcustomfieldsprocurify_python_sdktypecatalog_item_upsert_request_custom_fieldspy"></a>

##### description: `Optional[str]`<a id="description-optionalstr"></a>

##### id: `int`<a id="id-int"></a>

##### image: `str`<a id="image-str"></a>

##### unit_type: `str`<a id="unit_type-str"></a>

##### pref_vendor: `Optional[int]`<a id="pref_vendor-optionalint"></a>

##### account_code: `Optional[int]`<a id="account_code-optionalint"></a>

##### internal_sku: `str`<a id="internal_sku-str"></a>

##### product_url: `Optional[str]`<a id="product_url-optionalstr"></a>

##### price: `str`<a id="price-str"></a>

##### rfo_lock: `bool`<a id="rfo_lock-bool"></a>

##### departments: [`CatalogItemUpsertRequestDepartments`](./procurify_python_sdk/type/catalog_item_upsert_request_departments.py)<a id="departments-catalogitemupsertrequestdepartmentsprocurify_python_sdktypecatalog_item_upsert_request_departmentspy"></a>

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CatalogItemUpsertRequest`](./procurify_python_sdk/type/catalog_item_upsert_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CatalogItemReadSerializerSingleCreate`](./procurify_python_sdk/pydantic/catalog_item_read_serializer_single_create.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/catalog-items` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.catalog.update_item`<a id="procurifycatalogupdate_item"></a>

Update Catalog Item

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_item_response = procurify.catalog.update_item(
    name="a",
    currency=1,
    custom_fields=[
        {
            "key": None,
        }
    ],
    id=1,
    description="string_example",
    id=1,
    image="string_example",
    unit_type="string_example",
    pref_vendor=1,
    account_code=1,
    internal_sku="string_example",
    product_url="string_example",
    price="480728",
    rfo_lock=True,
    departments=[
        1
    ],
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

A unique integer value identifying this catalog items.

##### format: `str`<a id="format-str"></a>

##### requestBody: [`CatalogItemUpsertRequest`](./procurify_python_sdk/type/catalog_item_upsert_request.py)<a id="requestbody-catalogitemupsertrequestprocurify_python_sdktypecatalog_item_upsert_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CatalogItemReadSerializerSingleUpdate`](./procurify_python_sdk/pydantic/catalog_item_read_serializer_single_update.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/catalog-items/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.currencies.list`<a id="procurifycurrencieslist"></a>

Get Active/Inactive Currencies

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = procurify.currencies.list(
    active=True,
    base=True,
    description="string_example",
    format="csv",
    name="string_example",
    order_by="string_example",
    page=1,
    page_size=1,
    rate=3.14,
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### active: `bool`<a id="active-bool"></a>

##### base: `bool`<a id="base-bool"></a>

##### description: `str`<a id="description-str"></a>

##### format: `str`<a id="format-str"></a>

##### name: `str`<a id="name-str"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### rate: `Union[int, float]`<a id="rate-unionint-float"></a>

##### search: `str`<a id="search-str"></a>

A search term.

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedCurrencyList`](./procurify_python_sdk/pydantic/paginated_currency_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/currencies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.custom_fields.get_order_item_custom_fields`<a id="procurifycustom_fieldsget_order_item_custom_fields"></a>

Get list of custom fields associated with order items

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_order_item_custom_fields_response = procurify.custom_fields.get_order_item_custom_fields(
    field_type="a",
    format="csv",
    meta__is_active=True,
    page=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field_type: `str`<a id="field_type-str"></a>

##### format: `str`<a id="format-str"></a>

##### meta__is_active: `bool`<a id="meta__is_active-bool"></a>

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedCustomFieldReadList`](./procurify_python_sdk/pydantic/paginated_custom_field_read_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/custom-fields/order-items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.custom_fields.update_order_item_custom_field_dropdown_choices`<a id="procurifycustom_fieldsupdate_order_item_custom_field_dropdown_choices"></a>

 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_order_item_custom_field_dropdown_choices_response = procurify.custom_fields.update_order_item_custom_field_dropdown_choices(
    name="a",
    field_type="a",
    id=1,
    default_value="string_example",
    is_required=True,
    field_choices=[],
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### field_type: `str`<a id="field_type-str"></a>

##### id: `int`<a id="id-int"></a>

A unique integer value identifying this custom field.

##### default_value: `str`<a id="default_value-str"></a>

##### is_required: `bool`<a id="is_required-bool"></a>

##### field_choices: [`CustomFieldUpdateRequestFieldChoices`](./procurify_python_sdk/type/custom_field_update_request_field_choices.py)<a id="field_choices-customfieldupdaterequestfieldchoicesprocurify_python_sdktypecustom_field_update_request_field_choicespy"></a>

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldUpdateRequest`](./procurify_python_sdk/type/custom_field_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldReadSerializerSingle`](./procurify_python_sdk/pydantic/custom_field_read_serializer_single.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/custom-fields/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.departments.create`<a id="procurifydepartmentscreate"></a>

 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = procurify.departments.create(
    branch=1,
    name="a",
    external_id="string_example",
    active=True,
    punchout_email="a",
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### branch: `int`<a id="branch-int"></a>

##### name: `str`<a id="name-str"></a>

##### external_id: `Optional[str]`<a id="external_id-optionalstr"></a>

External id

##### active: `bool`<a id="active-bool"></a>

##### punchout_email: `Optional[str]`<a id="punchout_email-optionalstr"></a>

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentUpsertRequest`](./procurify_python_sdk/type/department_upsert_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentReadSerializerSingleCreate`](./procurify_python_sdk/pydantic/department_read_serializer_single_create.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/departments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.departments.list`<a id="procurifydepartmentslist"></a>

 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = procurify.departments.list(
    branch=1,
    format="csv",
    include_is_active_for_account_code=1,
    location_perm_override=True,
    locations=[
        1
    ],
    order_by="string_example",
    page=1,
    page_size=1,
    permission=1,
    requestable="string_example",
    search="string_example",
    user=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### branch: `int`<a id="branch-int"></a>

Filter departments by their branch.

##### format: `str`<a id="format-str"></a>

##### include_is_active_for_account_code: `int`<a id="include_is_active_for_account_code-int"></a>

Setting this adds the addition of the booeal field 'has_active_account' to each department object of the response. The query param accepts an integer representing the primary key of the account code to check if there exists an account object associated with the department with that account code.

##### location_perm_override: `bool`<a id="location_perm_override-bool"></a>

Setting this overrides the need to enable the PROCUREMENT_ACCESS and/or RECEIVE_BY_DEPARTMENT feature switches. This parameter can only be used in conjunction with permission and user and cannot function without both of those parameters explicitly set.

##### locations: List[`int`]<a id="locations-listint"></a>

Filter departments by the locations (branches) passed in.

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### permission: `int`<a id="permission-int"></a>

Filter by permission. In isolation, this parameter can only be set to 68 (add purchase order); 841 (view report); or 899 (receive_po), which correlate with permission to add purchase orders, view reports, and receive purchase orders respectively. However, the results returned correlate with the “by department” version of these permissions, which means that results are filtered by permission to add purchase orders by department, permission to view reports by department, and receive purchase orders by department. This should only be used in conjunction with the PROCUREMENT_ACCESS and/or RECEIVE_BY_DEPARTMENT feature switches. If used in conjunction with location_perm_override=true and user, the value can be set to any permission, and the result will be departments filtered by the provided user and permission values. If used in conjunction with the RECEIVE_BY_DEPARTMENT feature flag, the permission can only be set to 68, 841, or 899 (see second sentence for what these permissions do). The result will be all departments filtered by the provided user value.

##### requestable: `str`<a id="requestable-str"></a>

Fetch all requestable departments by the currently authorized user. Accepts ORDER, EXPENSE, TRAVEL, and PAY_REQUEST.

##### search: `str`<a id="search-str"></a>

A search term.

##### user: `int`<a id="user-int"></a>

Filter by user. If this parameter is set, the user must be a superuser or have the add_po_by_department or receive_po_by_department permissions. In isolation, this parameter should only be used in conjunction with the PROCUREMENT_ACCESS and/or RECEIVE_BY_DEPARTMENT feature switches. If used in conjunction with location_perm_override=true and permission query parameter, the result returned will be departments filtered by the provided user and permission values. If used in conjunction with the RECEIVE_BY_DEPARTMENT feature flag, the result will be departments filtered by the user provided and the permission set to 68 (add purchase order); 841 (view report); or 899 (receive purchase order) (see permission query parameter explanation for more information on what these stand for).

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedDepartmentReadList`](./procurify_python_sdk/pydantic/paginated_department_read_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/departments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.departments.update`<a id="procurifydepartmentsupdate"></a>

 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = procurify.departments.update(
    branch=1,
    name="a",
    id=1,
    external_id="string_example",
    active=True,
    punchout_email="a",
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### branch: `int`<a id="branch-int"></a>

##### name: `str`<a id="name-str"></a>

##### id: `int`<a id="id-int"></a>

A unique integer value identifying this department.

##### external_id: `Optional[str]`<a id="external_id-optionalstr"></a>

External id

##### active: `bool`<a id="active-bool"></a>

##### punchout_email: `Optional[str]`<a id="punchout_email-optionalstr"></a>

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentUpsertRequest`](./procurify_python_sdk/type/department_upsert_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentReadSerializerSingleUpdate`](./procurify_python_sdk/pydantic/department_read_serializer_single_update.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/departments/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.locations.create`<a id="procurifylocationscreate"></a>

Create New Location. Note: only users with superuser permission can create locations.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = procurify.locations.create(
    name="a",
    currency="a",
    phone_one="a",
    primary_billing_address={
        "name": "name_example",
        "address_line_one": "address_line_one_example",
        "city": "city_example",
        "postal_code": "postal_code_example",
        "country": "country_example",
    },
    primary_shipping_address={
        "name": "name_example",
        "address_line_one": "address_line_one_example",
        "city": "city_example",
        "postal_code": "postal_code_example",
        "country": "country_example",
    },
    shipping_addresses=[
        {
            "name": "name_example",
            "address_line_one": "address_line_one_example",
            "city": "city_example",
            "postal_code": "postal_code_example",
            "country": "country_example",
        }
    ],
    url="string_example",
    logo="string_example",
    fax="string_example",
    email="string_example",
    language=1,
    location_timezone=1,
    active=True,
    external_id="string_example",
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### currency: `str`<a id="currency-str"></a>

##### phone_one: `str`<a id="phone_one-str"></a>

##### primary_billing_address: [`AddressRequest`](./procurify_python_sdk/type/address_request.py)<a id="primary_billing_address-addressrequestprocurify_python_sdktypeaddress_requestpy"></a>


##### primary_shipping_address: [`AddressRequest`](./procurify_python_sdk/type/address_request.py)<a id="primary_shipping_address-addressrequestprocurify_python_sdktypeaddress_requestpy"></a>


##### shipping_addresses: List[`AddressRequest`]<a id="shipping_addresses-listaddressrequest"></a>

##### url: `Optional[str]`<a id="url-optionalstr"></a>

##### logo: `Optional[str]`<a id="logo-optionalstr"></a>

##### fax: `Optional[str]`<a id="fax-optionalstr"></a>

##### email: `Optional[str]`<a id="email-optionalstr"></a>

##### language: [`LanguageEnum`](./procurify_python_sdk/type/language_enum.py)<a id="language-languageenumprocurify_python_sdktypelanguage_enumpy"></a>

##### location_timezone: `Union[LocationTimezoneEnum, BlankEnum, NullEnum]`<a id="location_timezone-unionlocationtimezoneenum-blankenum-nullenum"></a>

##### active: `bool`<a id="active-bool"></a>

##### external_id: `Optional[str]`<a id="external_id-optionalstr"></a>

External id

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocationCreateUpsertRequest`](./procurify_python_sdk/type/location_create_upsert_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LocationViewSerializerSingleCreate`](./procurify_python_sdk/pydantic/location_view_serializer_single_create.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/locations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.locations.list`<a id="procurifylocationslist"></a>

Get Locations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = procurify.locations.list(
    active=True,
    format="csv",
    headquarter=True,
    order_by="string_example",
    page=1,
    page_size=1,
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### active: `bool`<a id="active-bool"></a>

##### format: `str`<a id="format-str"></a>

##### headquarter: `bool`<a id="headquarter-bool"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### search: `str`<a id="search-str"></a>

A search term.

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedLocationViewSerializerListList`](./procurify_python_sdk/pydantic/paginated_location_view_serializer_list_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.locations.retrieve`<a id="procurifylocationsretrieve"></a>

Get Location by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = procurify.locations.retrieve(
    id="id_example",
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### format: `str`<a id="format-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`LocationViewSerializerSingleRetrieve`](./procurify_python_sdk/pydantic/location_view_serializer_single_retrieve.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/locations/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.oauth.token_request`<a id="procurifyoauthtoken_request"></a>

Getting access to Procurify API involves the following three steps:

  1. Request credentials for your Procurify account.
  2. Request access token using your credentials.
  3. Use access token to access Procurify API resources.

#### Request credentials for your Procurify account.<a id="request-credentials-for-your-procurify-account"></a>

The first step is to request credentials from Procurify. Your role must have access to manage integrations settings in order to request API credentials. You can request API credentials by going to go:

  1. Settings in the left navigation bar.
  2. Integrations in the Tools section.
  3. View button beside API item

This page will allow you to enter an optional description of the application you are developing with the Procurify API and once you are ready, click on “Create Application”. On the next screen, you will be presented with a Client ID and a Client Secret. You will need to copy and save these credentials securely. Please note that the Client Secret is only presented once.

#### Request access token using your credentials.<a id="request-access-token-using-your-credentials"></a>

Once you have the client credentials, you will need to request an access token using these credentials that can be used as a bearer token when making a request to Procurify API. You will need the following information to request an access token:

|Info|Value|
--- | ---
|Token URL:|https://&lt;your-domain&gt;.procurify.com/oauth/token|
|Client ID:|*From the previous step*|
|Client Secret:|*From the previous step*|
|Audience:|https://api.procurify.com/|
|Grant Type:|client_credentials|

Once you have the access token, you will need to cache it until it expires (24 hrs). Please let Procurify support know if you would like help with this.


An example request and response using cURL (replace client id and client secret)

    $ curl -H "content-type: application/json" -X POST \
        -d '{"client_id": "~your_client_id~", \
             "client_secret": "~your_client_secret~", \
             "audience": "https://api.procurify.com/", \
             "grant_type": "client_credentials"}' \
        https://<your-domain>.procurify.com/oauth/token

    {"access_token": "~your-access-token~",
     "scope": "urn:procurify-api:domain:~your_domain~ urn:procurify-api:email:~your_email~",
     "expires_in": 86400,
     "token_type": "Bearer"}


#### Use access token to access Procurify API resources.<a id="use-access-token-to-access-procurify-api-resources"></a>

Once you have the access token, you can make requests to Procurify API resources. You will need to set the following headers when making the request.

|Key|Value|
--- | ---
|Authorization:|Bearer *access_token from previous step*|
|X-Procurify-Client:|api|


An example request and response using cURL (replace access token and your procurify domain)

    $ curl -H "Authorization: Bearer ~access_token~" \
        -H "X-Procurify-Client: api" \
        https://<your-domain>.procurify.com/api/v3/vendors/

        {"data":[{"id":1,"name":"OTHER","active":true,"addressLineOne":"OTHER"...}

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
token_request_response = procurify.oauth.token_request(
    client_id="string_example",
    client_secret="string_example",
    audience="string_example",
    grant_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### client_secret: `str`<a id="client_secret-str"></a>

##### audience: `str`<a id="audience-str"></a>

##### grant_type: `str`<a id="grant_type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OauthTokenRequestRequest`](./procurify_python_sdk/type/oauth_token_request_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OauthTokenRequestResponse`](./procurify_python_sdk/pydantic/oauth_token_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.order_items.list_items`<a id="procurifyorder_itemslist_items"></a>

**Order Item Status Codes**

| Order Item Type          | Code      | Description                       |
|--------------------------|-----------|-----------------------------------|
| PURCHASE_PENDING         | 0         | Approved but not purchased.       |
| PURCHASE_INUSE           | 1         | Added to purchaser's PO list.     |
| RECEIVE_PENDING          | 2         | Purchased but not yet received, i.e. receivedPassQty == 0. |
| RECEIVED                 | 3         | Fully received, i.e. receivedPassQty == quantity. |
| REJECTED_FOR_PURCHASE    | 4         | Rejected at procurement, i.e. denied. |
| RECEIVE_PARTIAL          | 5         | Partially received, i.e. receivedPassQty != quantity and receivedPassQty > 0. |
| FULFILLED                | 6         | Received but unused. |
| APPROVAL_DENIED          | 7         | Denied in approval routing (by approver). |
| REQUEST_DRAFT            | 8         | Preparing for draft instead of using sessions. |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_items_response = procurify.order_items.list_items(
    account=1,
    account_code=1,
    active=True,
    approved_datetime_0="1970-01-01",
    approved_datetime_1="1970-01-01",
    approved_price=3.14,
    approved_quantity=3.14,
    approver=3.14,
    approver_id=3.14,
    branch=1,
    catalog=True,
    catalog_item="string_example",
    currency=1,
    department=1,
    departments="string_example",
    exclude="string_example",
    exclude_punchout=True,
    format="csv",
    fulfilment_status="string_example",
    is_purchased=True,
    is_recurring=True,
    last_changed_by=1,
    last_modified_0="1970-01-01",
    last_modified_1="1970-01-01",
    line_comment="string_example",
    location=1,
    locations="string_example",
    name="string_example",
    num="string_example",
    order_num=1,
    order_num__status=0,
    order_by="string_example",
    order_created_date_0="1970-01-01",
    order_created_date_1="1970-01-01",
    page=1,
    page_size=1,
    po_created_date_0="1970-01-01",
    po_created_date_1="1970-01-01",
    po_vendor=1,
    pref_vendor=1,
    price=3.14,
    purchase_agreement=3.14,
    purchased_date_0="1970-01-01",
    purchased_date_1="1970-01-01",
    purchaser=1,
    quantity=3.14,
    received_fail_qty=3.14,
    received_pass_qty=3.14,
    requester=1,
    search="string_example",
    sku="string_example",
    status=0,
    type=0,
    unit="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account: `int`<a id="account-int"></a>

##### account_code: `int`<a id="account_code-int"></a>

Account Code

##### active: `bool`<a id="active-bool"></a>

##### approved_datetime_0: `date`<a id="approved_datetime_0-date"></a>

Approved Date

##### approved_datetime_1: `date`<a id="approved_datetime_1-date"></a>

Approved Date

##### approved_price: `Union[int, float]`<a id="approved_price-unionint-float"></a>

##### approved_quantity: `Union[int, float]`<a id="approved_quantity-unionint-float"></a>

##### approver: `Union[int, float]`<a id="approver-unionint-float"></a>

##### approver_id: `Union[int, float]`<a id="approver_id-unionint-float"></a>

##### branch: `int`<a id="branch-int"></a>

Location

##### catalog: `bool`<a id="catalog-bool"></a>

##### catalog_item: `str`<a id="catalog_item-str"></a>

A comma-separated list of integers.

##### currency: `int`<a id="currency-int"></a>

##### department: `int`<a id="department-int"></a>

Department

##### departments: `str`<a id="departments-str"></a>

A comma-separated list of integers.

##### exclude: `str`<a id="exclude-str"></a>

A comma-separated list of integers.

##### exclude_punchout: `bool`<a id="exclude_punchout-bool"></a>

##### format: `str`<a id="format-str"></a>

##### fulfilment_status: `str`<a id="fulfilment_status-str"></a>

##### is_purchased: `bool`<a id="is_purchased-bool"></a>

##### is_recurring: `bool`<a id="is_recurring-bool"></a>

##### last_changed_by: `int`<a id="last_changed_by-int"></a>

##### last_modified_0: `date`<a id="last_modified_0-date"></a>

Last Modified Date

##### last_modified_1: `date`<a id="last_modified_1-date"></a>

Last Modified Date

##### line_comment: `str`<a id="line_comment-str"></a>

##### location: `int`<a id="location-int"></a>

Location

##### locations: `str`<a id="locations-str"></a>

A comma-separated list of integers.

##### name: `str`<a id="name-str"></a>

##### num: `str`<a id="num-str"></a>

##### order_num: `int`<a id="order_num-int"></a>

##### order_num__status: `int`<a id="order_num__status-int"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### order_created_date_0: `date`<a id="order_created_date_0-date"></a>

Order Created Date

##### order_created_date_1: `date`<a id="order_created_date_1-date"></a>

Order Created Date

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### po_created_date_0: `date`<a id="po_created_date_0-date"></a>

Purchased Date

##### po_created_date_1: `date`<a id="po_created_date_1-date"></a>

Purchased Date

##### po_vendor: `int`<a id="po_vendor-int"></a>

Purchased Vendor

##### pref_vendor: `int`<a id="pref_vendor-int"></a>

##### price: `Union[int, float]`<a id="price-unionint-float"></a>

##### purchase_agreement: `Union[int, float]`<a id="purchase_agreement-unionint-float"></a>

##### purchased_date_0: `date`<a id="purchased_date_0-date"></a>

Purchased Date

##### purchased_date_1: `date`<a id="purchased_date_1-date"></a>

Purchased Date

##### purchaser: `int`<a id="purchaser-int"></a>

##### quantity: `Union[int, float]`<a id="quantity-unionint-float"></a>

##### received_fail_qty: `Union[int, float]`<a id="received_fail_qty-unionint-float"></a>

##### received_pass_qty: `Union[int, float]`<a id="received_pass_qty-unionint-float"></a>

##### requester: `int`<a id="requester-int"></a>

Requester

##### search: `str`<a id="search-str"></a>

A search term.

##### sku: `str`<a id="sku-str"></a>

##### status: `Optional[int]`<a id="status-optionalint"></a>

##### type: `int`<a id="type-int"></a>

##### unit: `str`<a id="unit-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedOrderItemList`](./procurify_python_sdk/pydantic/paginated_order_item_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/order-items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.permissions.get_available_system_roles`<a id="procurifypermissionsget_available_system_roles"></a>

Get Available System Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_available_system_roles_response = procurify.permissions.get_available_system_roles(
    format="csv",
    order_by="string_example",
    page=1,
    page_size=1,
    permission="string_example",
    search="string_example",
    type=1,
    user=1,
    userprofile=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### format: `str`<a id="format-str"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### permission: `str`<a id="permission-str"></a>

##### search: `str`<a id="search-str"></a>

A search term.

##### type: `int`<a id="type-int"></a>

##### user: `int`<a id="user-int"></a>

##### userprofile: `int`<a id="userprofile-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedPermissionGroupList`](./procurify_python_sdk/pydantic/paginated_permission_group_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/permissions/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.permissions.list`<a id="procurifypermissionslist"></a>

Get Available User Permissions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = procurify.permissions.list(
    format="csv",
    order_by="string_example",
    page=1,
    page_size=1,
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### format: `str`<a id="format-str"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### search: `str`<a id="search-str"></a>

A search term.

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedPermissionReadList`](./procurify_python_sdk/pydantic/paginated_permission_read_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/permissions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.purchase_orders.close_order`<a id="procurifypurchase_ordersclose_order"></a>

Close a Purchase Order

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
close_order_response = procurify.purchase_orders.close_order(
    procurify_po=1,
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### procurify_po: `int`<a id="procurify_po-int"></a>

A unique integer value identifying this po.

##### format: `str`<a id="format-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PurchaseOrderReadDocsSerializerSingle`](./procurify_python_sdk/pydantic/purchase_order_read_docs_serializer_single.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/purchase-orders/{procurify_PO}/close` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.purchase_orders.get_by_id_with_items`<a id="procurifypurchase_ordersget_by_id_with_items"></a>

**Purchase Order State Codes**

| Order Type          | Code      |
|---------------------|-----------|
| PURCHASED           | 0         |
| CANCELLED           | 1         |
| (legacy code)       | 2         |
| CLOSED              | 3         |
| PAID                | 4         |
| REOPENED            | 5         |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_with_items_response = procurify.purchase_orders.get_by_id_with_items(
    id="id_example",
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Procurify PO or UUID

##### format: `str`<a id="format-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApiNestedEditDeletePurchaseOrderDetail`](./procurify_python_sdk/pydantic/api_nested_edit_delete_purchase_order_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/purchase_orders/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.purchase_orders.get_by_role_and_status`<a id="procurifypurchase_ordersget_by_role_and_status"></a>

Get Purchase Orders by Role & Status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_role_and_status_response = procurify.purchase_orders.get_by_role_and_status(
    role="purchased",
    status="all",
    contract=1,
    date_0="1970-01-01",
    date_1="1970-01-01",
    expiry_date_0="1970-01-01",
    expiry_date_1="1970-01-01",
    has_blanket_order_items=True,
    modified_date_0="1970-01-01",
    modified_date_1="1970-01-01",
    order_by="string_example",
    page=1,
    page_size=1,
    pref_vendor=1,
    promise_date_0="1970-01-01",
    promise_date_1="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### role: `str`<a id="role-str"></a>

##### status: `str`<a id="status-str"></a>

##### contract: `int`<a id="contract-int"></a>

Contract

##### date_0: `date`<a id="date_0-date"></a>

YYYY-MM-DD (start date): Filter POs by Created Date range

##### date_1: `date`<a id="date_1-date"></a>

YYYY-MM-DD (end date): Filter POs by Created Date range

##### expiry_date_0: `date`<a id="expiry_date_0-date"></a>

Expiry Date

##### expiry_date_1: `date`<a id="expiry_date_1-date"></a>

Expiry Date

##### has_blanket_order_items: `bool`<a id="has_blanket_order_items-bool"></a>

##### modified_date_0: `date`<a id="modified_date_0-date"></a>

YYYY-MM-DD (start date): Filter POs by Last Modified Date range

##### modified_date_1: `date`<a id="modified_date_1-date"></a>

YYYY-MM-DD (end date): Filter POs by Last Modified Date range

##### order_by: `str`<a id="order_by-str"></a>

Sort by field

##### page: `int`<a id="page-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### pref_vendor: `int`<a id="pref_vendor-int"></a>

ID of Vendor

##### promise_date_0: `date`<a id="promise_date_0-date"></a>

YYYY-MM-DD (start date): Filter POs by Promise Date range

##### promise_date_1: `date`<a id="promise_date_1-date"></a>

YYYY-MM-DD (end date): Filter POs by Promise Date range

#### 🔄 Return<a id="🔄-return"></a>

[`POWithListPurchaseOrderDocs`](./procurify_python_sdk/pydantic/po_with_list_purchase_order_docs.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/purchase_orders/{role}/{status}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.purchase_orders.reopen_procurify_po`<a id="procurifypurchase_ordersreopen_procurify_po"></a>

Reopen a Purchase Order

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
procurify.purchase_orders.reopen_procurify_po(
    procurify_po=1,
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### procurify_po: `int`<a id="procurify_po-int"></a>

A unique integer value identifying this po.

##### format: `str`<a id="format-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/purchase-orders/{procurify_PO}/reopen` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.purchase_orders.revise_procurify_po`<a id="procurifypurchase_ordersrevise_procurify_po"></a>

Deprecated method for revising a purchase order. Pending removable after November 16, 2023. Use `PUT` on `/api/v3/purchase-orders/{id}` instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
revise_procurify_po_response = procurify.purchase_orders.revise_procurify_po(
    version=1,
    order_items=[
        {
            "id": 1,
            "name": "name_example",
            "unit": "unit_example",
            "quantity": "480728",
            "price": "480728",
            "custom_fields": [
                {
                    "key": None,
                }
            ],
        }
    ],
    buyer_name="a",
    buyer_contact="a",
    buyer_address_line_one="a",
    buyer_postal_code="a",
    buyer_city="a",
    buyer_country="a",
    buyer_address=1,
    receiver_name="a",
    receiver_contact="a",
    receiver_address_line_one="a",
    receiver_postal_code="a",
    receiver_city="a",
    receiver_country="a",
    receiver_address=1,
    promise_date="1970-01-01T00:00:00.00Z",
    discount={
        "key": None,
    },
    tax={
        "key": None,
    },
    procurify_po=1,
    custom_fields=[],
    po_num="string_example",
    buyer_state_province="string_example",
    comment="string_example",
    receiver_state_province="string_example",
    freight="480728",
    other="480728",
    disclaimer_description="string_example",
    disclaimer_text="string_example",
    payment_term_ref=1,
    shipping_term_ref=1,
    payment_method_ref=1,
    shipping_method_ref=1,
    creditcard=1,
    expiry_date="1970-01-01T00:00:00.00Z",
    contract=1,
    confirm_duplicate_external_po_number="False",
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `int`<a id="version-int"></a>

##### order_items: List[`OrderItemPurchaseEditRequest`]<a id="order_items-listorderitempurchaseeditrequest"></a>

##### buyer_name: `str`<a id="buyer_name-str"></a>

##### buyer_contact: `str`<a id="buyer_contact-str"></a>

##### buyer_address_line_one: `str`<a id="buyer_address_line_one-str"></a>

##### buyer_postal_code: `str`<a id="buyer_postal_code-str"></a>

##### buyer_city: `str`<a id="buyer_city-str"></a>

##### buyer_country: `str`<a id="buyer_country-str"></a>

##### buyer_address: `int`<a id="buyer_address-int"></a>

##### receiver_name: `str`<a id="receiver_name-str"></a>

##### receiver_contact: `str`<a id="receiver_contact-str"></a>

##### receiver_address_line_one: `str`<a id="receiver_address_line_one-str"></a>

##### receiver_postal_code: `str`<a id="receiver_postal_code-str"></a>

##### receiver_city: `str`<a id="receiver_city-str"></a>

##### receiver_country: `str`<a id="receiver_country-str"></a>

##### receiver_address: `int`<a id="receiver_address-int"></a>

##### promise_date: `datetime`<a id="promise_date-datetime"></a>

##### discount: [`PurchaseOrderUpdateRequestDiscount`](./procurify_python_sdk/type/purchase_order_update_request_discount.py)<a id="discount-purchaseorderupdaterequestdiscountprocurify_python_sdktypepurchase_order_update_request_discountpy"></a>

##### tax: [`PurchaseOrderUpdateRequestTax`](./procurify_python_sdk/type/purchase_order_update_request_tax.py)<a id="tax-purchaseorderupdaterequesttaxprocurify_python_sdktypepurchase_order_update_request_taxpy"></a>

##### procurify_po: `int`<a id="procurify_po-int"></a>

A unique integer value identifying this po.

##### custom_fields: [`PurchaseOrderUpdateRequestCustomFields`](./procurify_python_sdk/type/purchase_order_update_request_custom_fields.py)<a id="custom_fields-purchaseorderupdaterequestcustomfieldsprocurify_python_sdktypepurchase_order_update_request_custom_fieldspy"></a>

##### po_num: `Optional[str]`<a id="po_num-optionalstr"></a>

##### buyer_state_province: `str`<a id="buyer_state_province-str"></a>

##### comment: `Optional[str]`<a id="comment-optionalstr"></a>

##### receiver_state_province: `str`<a id="receiver_state_province-str"></a>

##### freight: `Optional[str]`<a id="freight-optionalstr"></a>

##### other: `Optional[str]`<a id="other-optionalstr"></a>

##### disclaimer_description: `Optional[str]`<a id="disclaimer_description-optionalstr"></a>

##### disclaimer_text: `Optional[str]`<a id="disclaimer_text-optionalstr"></a>

##### payment_term_ref: `Optional[int]`<a id="payment_term_ref-optionalint"></a>

##### shipping_term_ref: `Optional[int]`<a id="shipping_term_ref-optionalint"></a>

##### payment_method_ref: `Optional[int]`<a id="payment_method_ref-optionalint"></a>

##### shipping_method_ref: `Optional[int]`<a id="shipping_method_ref-optionalint"></a>

##### creditcard: `Optional[int]`<a id="creditcard-optionalint"></a>

##### expiry_date: `Optional[datetime]`<a id="expiry_date-optionaldatetime"></a>

##### contract: `Optional[int]`<a id="contract-optionalint"></a>

##### confirm_duplicate_external_po_number: `str`<a id="confirm_duplicate_external_po_number-str"></a>

Mechanism to check for duplicate custom PO number. If there is a duplicate, API will fail unless this query param is set to True.

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PurchaseOrderUpdateRequest`](./procurify_python_sdk/type/purchase_order_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PurchaseOrderDetailSerializerSingle`](./procurify_python_sdk/pydantic/purchase_order_detail_serializer_single.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/purchase_order/revise/{procurify_PO}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.purchase_orders.update_order`<a id="procurifypurchase_ordersupdate_order"></a>

Update a Purchase Order

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_order_response = procurify.purchase_orders.update_order(
    version=1,
    order_items=[
        {
            "id": 1,
            "name": "name_example",
            "unit": "unit_example",
            "quantity": "480728",
            "price": "480728",
            "custom_fields": [
                {
                    "key": None,
                }
            ],
        }
    ],
    buyer_name="a",
    buyer_contact="a",
    buyer_address_line_one="a",
    buyer_postal_code="a",
    buyer_city="a",
    buyer_country="a",
    buyer_address=1,
    receiver_name="a",
    receiver_contact="a",
    receiver_address_line_one="a",
    receiver_postal_code="a",
    receiver_city="a",
    receiver_country="a",
    receiver_address=1,
    promise_date="1970-01-01T00:00:00.00Z",
    discount={
        "key": None,
    },
    tax={
        "key": None,
    },
    procurify_po=1,
    custom_fields=[],
    po_num="string_example",
    buyer_state_province="string_example",
    comment="string_example",
    receiver_state_province="string_example",
    freight="480728",
    other="480728",
    disclaimer_description="string_example",
    disclaimer_text="string_example",
    payment_term_ref=1,
    shipping_term_ref=1,
    payment_method_ref=1,
    shipping_method_ref=1,
    creditcard=1,
    expiry_date="1970-01-01T00:00:00.00Z",
    contract=1,
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `int`<a id="version-int"></a>

##### order_items: List[`OrderItemPurchaseEditRequest`]<a id="order_items-listorderitempurchaseeditrequest"></a>

##### buyer_name: `str`<a id="buyer_name-str"></a>

##### buyer_contact: `str`<a id="buyer_contact-str"></a>

##### buyer_address_line_one: `str`<a id="buyer_address_line_one-str"></a>

##### buyer_postal_code: `str`<a id="buyer_postal_code-str"></a>

##### buyer_city: `str`<a id="buyer_city-str"></a>

##### buyer_country: `str`<a id="buyer_country-str"></a>

##### buyer_address: `int`<a id="buyer_address-int"></a>

##### receiver_name: `str`<a id="receiver_name-str"></a>

##### receiver_contact: `str`<a id="receiver_contact-str"></a>

##### receiver_address_line_one: `str`<a id="receiver_address_line_one-str"></a>

##### receiver_postal_code: `str`<a id="receiver_postal_code-str"></a>

##### receiver_city: `str`<a id="receiver_city-str"></a>

##### receiver_country: `str`<a id="receiver_country-str"></a>

##### receiver_address: `int`<a id="receiver_address-int"></a>

##### promise_date: `datetime`<a id="promise_date-datetime"></a>

##### discount: [`PurchaseOrderUpdateRequestDiscount`](./procurify_python_sdk/type/purchase_order_update_request_discount.py)<a id="discount-purchaseorderupdaterequestdiscountprocurify_python_sdktypepurchase_order_update_request_discountpy"></a>

##### tax: [`PurchaseOrderUpdateRequestTax`](./procurify_python_sdk/type/purchase_order_update_request_tax.py)<a id="tax-purchaseorderupdaterequesttaxprocurify_python_sdktypepurchase_order_update_request_taxpy"></a>

##### procurify_po: `int`<a id="procurify_po-int"></a>

A unique integer value identifying this po.

##### custom_fields: [`PurchaseOrderUpdateRequestCustomFields`](./procurify_python_sdk/type/purchase_order_update_request_custom_fields.py)<a id="custom_fields-purchaseorderupdaterequestcustomfieldsprocurify_python_sdktypepurchase_order_update_request_custom_fieldspy"></a>

##### po_num: `Optional[str]`<a id="po_num-optionalstr"></a>

##### buyer_state_province: `str`<a id="buyer_state_province-str"></a>

##### comment: `Optional[str]`<a id="comment-optionalstr"></a>

##### receiver_state_province: `str`<a id="receiver_state_province-str"></a>

##### freight: `Optional[str]`<a id="freight-optionalstr"></a>

##### other: `Optional[str]`<a id="other-optionalstr"></a>

##### disclaimer_description: `Optional[str]`<a id="disclaimer_description-optionalstr"></a>

##### disclaimer_text: `Optional[str]`<a id="disclaimer_text-optionalstr"></a>

##### payment_term_ref: `Optional[int]`<a id="payment_term_ref-optionalint"></a>

##### shipping_term_ref: `Optional[int]`<a id="shipping_term_ref-optionalint"></a>

##### payment_method_ref: `Optional[int]`<a id="payment_method_ref-optionalint"></a>

##### shipping_method_ref: `Optional[int]`<a id="shipping_method_ref-optionalint"></a>

##### creditcard: `Optional[int]`<a id="creditcard-optionalint"></a>

##### expiry_date: `Optional[datetime]`<a id="expiry_date-optionaldatetime"></a>

##### contract: `Optional[int]`<a id="contract-optionalint"></a>

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PurchaseOrderUpdateRequest`](./procurify_python_sdk/type/purchase_order_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PurchaseOrderUpdateSerializerSingle`](./procurify_python_sdk/pydantic/purchase_order_update_serializer_single.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/purchase-orders/{procurify_PO}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.purchase_orders.view_billing_history`<a id="procurifypurchase_ordersview_billing_history"></a>

View billing history of a Purchase Order

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
view_billing_history_response = procurify.purchase_orders.view_billing_history(
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### format: `str`<a id="format-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PurchaseOrderBillingHistorySerializerList`](./procurify_python_sdk/pydantic/purchase_order_billing_history_serializer_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/purchase-orders/billing-history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.requisitions.create`<a id="procurifyrequisitionscreate"></a>

Creating a requisition

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = procurify.requisitions.create(
    required_date="1970-01-01",
    location_name="a",
    department_name="a",
    line_items=[
        {
            "item_name": "item_name_example",
            "vendor_name": "vendor_name_example",
            "account_code": "account_code_example",
            "unit_price": "480728",
            "quantity": "480728",
            "unit": "unit_example",
            "currency_code": "currency_code_example",
            "custom_fields": [
                {
                    "custom_field_name": "custom_field_name_example",
                    "custom_field_value": "custom_field_value_example",
                }
            ],
        }
    ],
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required_date: `date`<a id="required_date-date"></a>

##### location_name: `str`<a id="location_name-str"></a>

##### department_name: `str`<a id="department_name-str"></a>

##### line_items: List[`RequisitionLineCreateRequest`]<a id="line_items-listrequisitionlinecreaterequest"></a>

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RequisitionCreateRequest`](./procurify_python_sdk/type/requisition_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RequisitionReadSerializerSingle`](./procurify_python_sdk/pydantic/requisition_read_serializer_single.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/requisitions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.requisitions.get_all_order_items`<a id="procurifyrequisitionsget_all_order_items"></a>

**Order Item Status Codes**

| Order Item Type          | Code      | Description                       |
|--------------------------|-----------|-----------------------------------|
| PURCHASE_PENDING         | 0         | Approved but not purchased.       |
| PURCHASE_INUSE           | 1         | Added to purchaser's PO list.     |
| RECEIVE_PENDING          | 2         | Purchased but not yet received, i.e. receivedPassQty == 0. |
| RECEIVED                 | 3         | Fully received, i.e. receivedPassQty == quantity. |
| REJECTED_FOR_PURCHASE    | 4         | Rejected at procurement, i.e. denied. |
| RECEIVE_PARTIAL          | 5         | Partially received, i.e. receivedPassQty != quantity and receivedPassQty > 0. |
| FULFILLED                | 6         | Received but unused. |
| APPROVAL_DENIED          | 7         | Denied in approval routing (by approver). |
| REQUEST_DRAFT            | 8         | Preparing for draft instead of using sessions. |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_order_items_response = procurify.requisitions.get_all_order_items(
    account=1,
    account_code=1,
    active=True,
    approved_datetime_0="1970-01-01",
    approved_datetime_1="1970-01-01",
    approved_price=3.14,
    approved_quantity=3.14,
    approver=3.14,
    approver_id=3.14,
    branch=1,
    catalog=True,
    catalog_item="string_example",
    currency=1,
    department=1,
    departments="string_example",
    exclude="string_example",
    exclude_punchout=True,
    format="csv",
    fulfilment_status="string_example",
    is_purchased=True,
    is_recurring=True,
    last_changed_by=1,
    last_modified_0="1970-01-01",
    last_modified_1="1970-01-01",
    line_comment="string_example",
    location=1,
    locations="string_example",
    name="string_example",
    num="string_example",
    order_num=1,
    order_num__status=0,
    order_by="string_example",
    order_created_date_0="1970-01-01",
    order_created_date_1="1970-01-01",
    page=1,
    page_size=1,
    po_created_date_0="1970-01-01",
    po_created_date_1="1970-01-01",
    po_vendor=1,
    pref_vendor=1,
    price=3.14,
    purchase_agreement=3.14,
    purchased_date_0="1970-01-01",
    purchased_date_1="1970-01-01",
    purchaser=1,
    quantity=3.14,
    received_fail_qty=3.14,
    received_pass_qty=3.14,
    requester=1,
    search="string_example",
    sku="string_example",
    status=0,
    type=0,
    unit="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account: `int`<a id="account-int"></a>

##### account_code: `int`<a id="account_code-int"></a>

Account Code

##### active: `bool`<a id="active-bool"></a>

##### approved_datetime_0: `date`<a id="approved_datetime_0-date"></a>

Approved Date

##### approved_datetime_1: `date`<a id="approved_datetime_1-date"></a>

Approved Date

##### approved_price: `Union[int, float]`<a id="approved_price-unionint-float"></a>

##### approved_quantity: `Union[int, float]`<a id="approved_quantity-unionint-float"></a>

##### approver: `Union[int, float]`<a id="approver-unionint-float"></a>

##### approver_id: `Union[int, float]`<a id="approver_id-unionint-float"></a>

##### branch: `int`<a id="branch-int"></a>

Location

##### catalog: `bool`<a id="catalog-bool"></a>

##### catalog_item: `str`<a id="catalog_item-str"></a>

A comma-separated list of integers.

##### currency: `int`<a id="currency-int"></a>

##### department: `int`<a id="department-int"></a>

Department

##### departments: `str`<a id="departments-str"></a>

A comma-separated list of integers.

##### exclude: `str`<a id="exclude-str"></a>

A comma-separated list of integers.

##### exclude_punchout: `bool`<a id="exclude_punchout-bool"></a>

##### format: `str`<a id="format-str"></a>

##### fulfilment_status: `str`<a id="fulfilment_status-str"></a>

##### is_purchased: `bool`<a id="is_purchased-bool"></a>

##### is_recurring: `bool`<a id="is_recurring-bool"></a>

##### last_changed_by: `int`<a id="last_changed_by-int"></a>

##### last_modified_0: `date`<a id="last_modified_0-date"></a>

Last Modified Date

##### last_modified_1: `date`<a id="last_modified_1-date"></a>

Last Modified Date

##### line_comment: `str`<a id="line_comment-str"></a>

##### location: `int`<a id="location-int"></a>

Location

##### locations: `str`<a id="locations-str"></a>

A comma-separated list of integers.

##### name: `str`<a id="name-str"></a>

##### num: `str`<a id="num-str"></a>

##### order_num: `int`<a id="order_num-int"></a>

##### order_num__status: `int`<a id="order_num__status-int"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### order_created_date_0: `date`<a id="order_created_date_0-date"></a>

Order Created Date

##### order_created_date_1: `date`<a id="order_created_date_1-date"></a>

Order Created Date

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### po_created_date_0: `date`<a id="po_created_date_0-date"></a>

Purchased Date

##### po_created_date_1: `date`<a id="po_created_date_1-date"></a>

Purchased Date

##### po_vendor: `int`<a id="po_vendor-int"></a>

Purchased Vendor

##### pref_vendor: `int`<a id="pref_vendor-int"></a>

##### price: `Union[int, float]`<a id="price-unionint-float"></a>

##### purchase_agreement: `Union[int, float]`<a id="purchase_agreement-unionint-float"></a>

##### purchased_date_0: `date`<a id="purchased_date_0-date"></a>

Purchased Date

##### purchased_date_1: `date`<a id="purchased_date_1-date"></a>

Purchased Date

##### purchaser: `int`<a id="purchaser-int"></a>

##### quantity: `Union[int, float]`<a id="quantity-unionint-float"></a>

##### received_fail_qty: `Union[int, float]`<a id="received_fail_qty-unionint-float"></a>

##### received_pass_qty: `Union[int, float]`<a id="received_pass_qty-unionint-float"></a>

##### requester: `int`<a id="requester-int"></a>

Requester

##### search: `str`<a id="search-str"></a>

A search term.

##### sku: `str`<a id="sku-str"></a>

##### status: `Optional[int]`<a id="status-optionalint"></a>

##### type: `int`<a id="type-int"></a>

##### unit: `str`<a id="unit-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedOrderItemList`](./procurify_python_sdk/pydantic/paginated_order_item_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/global/order_items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.requisitions.get_all_orders`<a id="procurifyrequisitionsget_all_orders"></a>

**Order Status Codes**

| Order Type          | Code      |
|---------------------|-----------|
| PENDING             | 0         |
| APPROVED            | 1         |
| REJECTED            | 2         |
| PURCHASED           | 3         |
| CANCELLED (legacy)  | 4         |
| RECEIVED            | 5         |
| DRAFT               | 6         |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_orders_response = procurify.requisitions.get_all_orders(
    branch=1,
    date_required="1970-01-01T00:00:00.00Z",
    date_0="1970-01-01",
    date_1="1970-01-01",
    department=1,
    format="csv",
    has_blanket_order_items=True,
    is_punchout=True,
    line_count=1,
    location=1,
    modified_date_0="1970-01-01",
    modified_date_1="1970-01-01",
    order_by="string_example",
    page=1,
    page_size=1,
    required_date_0="1970-01-01",
    required_date_1="1970-01-01",
    search="string_example",
    status=0,
    total_price=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### branch: `int`<a id="branch-int"></a>

##### date_required: `datetime`<a id="date_required-datetime"></a>

##### date_0: `date`<a id="date_0-date"></a>

Date

##### date_1: `date`<a id="date_1-date"></a>

Date

##### department: `int`<a id="department-int"></a>

##### format: `str`<a id="format-str"></a>

##### has_blanket_order_items: `bool`<a id="has_blanket_order_items-bool"></a>

##### is_punchout: `bool`<a id="is_punchout-bool"></a>

##### line_count: `int`<a id="line_count-int"></a>

##### location: `int`<a id="location-int"></a>

##### modified_date_0: `date`<a id="modified_date_0-date"></a>

Last Modified Date

##### modified_date_1: `date`<a id="modified_date_1-date"></a>

Last Modified Date

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### required_date_0: `date`<a id="required_date_0-date"></a>

Date Required

##### required_date_1: `date`<a id="required_date_1-date"></a>

Date Required

##### search: `str`<a id="search-str"></a>

A search term.

##### status: `int`<a id="status-int"></a>

##### total_price: `Union[int, float]`<a id="total_price-unionint-float"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedOrderReadList`](./procurify_python_sdk/pydantic/paginated_order_read_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/global/orders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.users.create`<a id="procurifyuserscreate"></a>

Create New User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = procurify.users.create(
    body=[
        {
            "email": "email_example",
            "send_invitation_email": True,
            "first_name": "",
            "last_name": "",
            "phone": "",
            "position": "",
            "role_id": 0,
            "all_locations": False,
            "locations": [],
            "home_department": 0,
            "home_location": 0,
        }
    ],
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### format: `str`<a id="format-str"></a>

##### requestBody: [`UsersCreateRequest`](./procurify_python_sdk/type/users_create_request.py)<a id="requestbody-userscreaterequestprocurify_python_sdktypeusers_create_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserProfileUnoptimizedSerializerList`](./procurify_python_sdk/pydantic/user_profile_unoptimized_serializer_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.users.destroy`<a id="procurifyusersdestroy"></a>

Deactivate User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
procurify.users.destroy(
    id=1,
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

A unique integer value identifying this user profile.

##### format: `str`<a id="format-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/users/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.users.get_logged_in_user`<a id="procurifyusersget_logged_in_user"></a>

Get the logged in user account information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_logged_in_user_response = procurify.users.get_logged_in_user(
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### format: `str`<a id="format-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserProfileMeSerializerSingle`](./procurify_python_sdk/pydantic/user_profile_me_serializer_single.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/users/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.users.list`<a id="procurifyuserslist"></a>

List Users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = procurify.users.list(
    format="csv",
    is_active=True,
    location="string_example",
    order_by="string_example",
    page=1,
    page_size=1,
    pending_invite=True,
    permission="string_example",
    role=3.14,
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### format: `str`<a id="format-str"></a>

##### is_active: `bool`<a id="is_active-bool"></a>

##### location: `str`<a id="location-str"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### pending_invite: `bool`<a id="pending_invite-bool"></a>

##### permission: `str`<a id="permission-str"></a>

##### role: `Union[int, float]`<a id="role-unionint-float"></a>

##### search: `str`<a id="search-str"></a>

A search term.

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedUserProfileUnoptimizedList`](./procurify_python_sdk/pydantic/paginated_user_profile_unoptimized_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.users.update`<a id="procurifyusersupdate"></a>

Update User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = procurify.users.update(
    email="a",
    first_name="a",
    last_name="a",
    location=1,
    department=1,
    id=1,
    id=1,
    user=1,
    position="",
    phone="",
    profile_image="string_example",
    is_sso_enabled=False,
    mark_for_skip=False,
    mark_for_delete=False,
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

A unique integer value identifying this user profile.

##### format: `str`<a id="format-str"></a>

##### requestBody: [`UserProfileUpsertRequest`](./procurify_python_sdk/type/user_profile_upsert_request.py)<a id="requestbody-userprofileupsertrequestprocurify_python_sdktypeuser_profile_upsert_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserProfileUnoptimizedSerializerSingle`](./procurify_python_sdk/pydantic/user_profile_unoptimized_serializer_single.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/users/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.vendors.create`<a id="procurifyvendorscreate"></a>

Create a new vendor

Due to having multiple vendors with the same name, especially
common if user keeps deleting vendors with the same name, these
deleted vendors get thrown into the inactive list.

**Vendor Types**

| Vendor Type         | Type      |
|---------------------|-----------|
| OTHER               | 1         |
| HIDDEN              | 2         |
| PREFERRED (default) | 3         |
| REGULAR             | 4         |
| EMPLOYEE            | 5         |
| CC_PROVIDER         | 6         |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = procurify.vendors.create(
    name="a",
    email=[
        "a"
    ],
    type=2,
    overall_score="48",
    active=True,
    address_line_one="string_example",
    address_line_two="string_example",
    postal_code="string_example",
    city="string_example",
    state_province="string_example",
    country="string_example",
    phone_one="string_example",
    phone_two="string_example",
    fax="string_example",
    comments="string_example",
    contact="string_example",
    url="string_example",
    external_id="string_example",
    currency=1,
    payment_term_ref={
        "name": "name_example",
    },
    shipping_term_ref={
        "name": "name_example",
    },
    payment_method_ref={
        "name": "name_example",
    },
    shipping_method_ref={
        "name": "name_example",
    },
    tax=1,
    default_payment_method=1,
    is_1099_eligible=True,
    is_auto_email_po_enabled=True,
    po_pdf_labels="string_example",
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the vendor

##### email: [`OptimizedVendorRequestEmail`](./procurify_python_sdk/type/optimized_vendor_request_email.py)<a id="email-optimizedvendorrequestemailprocurify_python_sdktypeoptimized_vendor_request_emailpy"></a>

##### type: [`VendorTypeEnum`](./procurify_python_sdk/type/vendor_type_enum.py)<a id="type-vendortypeenumprocurify_python_sdktypevendor_type_enumpy"></a>

##### overall_score: `Optional[str]`<a id="overall_score-optionalstr"></a>

##### active: `bool`<a id="active-bool"></a>

##### address_line_one: `Optional[str]`<a id="address_line_one-optionalstr"></a>

First line of address

##### address_line_two: `Optional[str]`<a id="address_line_two-optionalstr"></a>

Second line of address

##### postal_code: `Optional[str]`<a id="postal_code-optionalstr"></a>

Postal or Zip code of the vendor

##### city: `Optional[str]`<a id="city-optionalstr"></a>

City of the vendor

##### state_province: `Optional[str]`<a id="state_province-optionalstr"></a>

State or Province of the vendor

##### country: `Optional[str]`<a id="country-optionalstr"></a>

Country of the vendor

##### phone_one: `Optional[str]`<a id="phone_one-optionalstr"></a>

Primary phone no. of the vendor

##### phone_two: `Optional[str]`<a id="phone_two-optionalstr"></a>

Secondary phone no. of the vendor

##### fax: `Optional[str]`<a id="fax-optionalstr"></a>

Fax no. of the vendor

##### comments: `Optional[str]`<a id="comments-optionalstr"></a>

Notes about the vendor

##### contact: `Optional[str]`<a id="contact-optionalstr"></a>

Contact person of the vendor

##### url: `Optional[str]`<a id="url-optionalstr"></a>

Website of the vendor

##### external_id: `Optional[str]`<a id="external_id-optionalstr"></a>

External id of the vendor

##### currency: `Optional[int]`<a id="currency-optionalint"></a>

##### payment_term_ref: [`PaymentTermRequestNullable`](./procurify_python_sdk/type/payment_term_request_nullable.py)<a id="payment_term_ref-paymenttermrequestnullableprocurify_python_sdktypepayment_term_request_nullablepy"></a>


##### shipping_term_ref: [`ShippingTermRequestNullable`](./procurify_python_sdk/type/shipping_term_request_nullable.py)<a id="shipping_term_ref-shippingtermrequestnullableprocurify_python_sdktypeshipping_term_request_nullablepy"></a>


##### payment_method_ref: [`PaymentMethodRequestNullable`](./procurify_python_sdk/type/payment_method_request_nullable.py)<a id="payment_method_ref-paymentmethodrequestnullableprocurify_python_sdktypepayment_method_request_nullablepy"></a>


##### shipping_method_ref: [`ShippingMethodRequestNullable`](./procurify_python_sdk/type/shipping_method_request_nullable.py)<a id="shipping_method_ref-shippingmethodrequestnullableprocurify_python_sdktypeshipping_method_request_nullablepy"></a>


##### tax: `Optional[int]`<a id="tax-optionalint"></a>

##### default_payment_method: `Optional[int]`<a id="default_payment_method-optionalint"></a>

##### is_1099_eligible: `Optional[bool]`<a id="is_1099_eligible-optionalbool"></a>

##### is_auto_email_po_enabled: `bool`<a id="is_auto_email_po_enabled-bool"></a>

##### po_pdf_labels: `str`<a id="po_pdf_labels-str"></a>

Placeholder for a KVStore value

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OptimizedVendorRequest`](./procurify_python_sdk/type/optimized_vendor_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VendorDetailSerializerSingleCreate`](./procurify_python_sdk/pydantic/vendor_detail_serializer_single_create.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/vendors` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.vendors.list`<a id="procurifyvendorslist"></a>

**Vendor Type Codes**

| Vendor Type         | Type      | Description                       |
|---------------------|-----------|-----------------------------------|
| OTHER               | 1         | Previously 'OTHER' vendor (ID=1), used for storing non-vendor
|                     |           | for storing non-vendor Vendor names in request. |
| HIDDEN              | 2         | New type of vendors that is reserved for system purposes (eg. Amazon Business). |
| PREFERRED (default) | 3         | The default vendors from previous list
|                     |           | where active vendor dropdowns everywhere previously showed.
|                     |           | Request now ONLY shows these vendors (+OTHER) |
| REGULAR             | 4         | New type of vendors that are non-preferred,
|                     |           | for any AP purposes and purchasers to update.
|                     |           | (DOES NOT show up in Request, but shows up in Procure) |
| EMPLOYEE            | 5         | New type of vendors that do not show up anywhere except in AP employees list. |
| CC_PROVIDER         | 6         | Similar type of vendors to AP employees, but for AP credit card providers. |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = procurify.vendors.list(
    vendor_group="all",
    exclude_other=True,
    external_id="string_example",
    format="csv",
    name="string_example",
    order_by="string_example",
    page=1,
    page_size=1,
    search="string_example",
    type=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### vendor_group: `str`<a id="vendor_group-str"></a>

 **\"all\"**: Get list of all vendors.  **\"credit_card_providers\"**: Get list of credit card provider vendors. These vendors are displayed in Payee Management for Credit Card Providers.  **\"default\"**: Get list of \"preferred\" and \"regular\" vendors. These vendors are displayed in Procure (procurement, vendors, etc) and AP i.e., default vendor list. OTHER is discontinued from procure.  **\"other\"**: Get list of \"other\" vendors. Only returns the 'OTHER' vendor reserved for requesting non-vendor names.  **\"preferred\"**: Get list of \"preferred\" vendors.  **\"purchasable\"**: Get list of \"purchasable\" vendors.  **\"requestable\"**: Get list of \"requestable\" vendors. These vendors are displayed in Request and designated by Purchaser.

##### exclude_other: `bool`<a id="exclude_other-bool"></a>

##### external_id: `str`<a id="external_id-str"></a>

##### format: `str`<a id="format-str"></a>

##### name: `str`<a id="name-str"></a>

##### order_by: `str`<a id="order_by-str"></a>

Which field to use when ordering the results.

##### page: `int`<a id="page-int"></a>

A page number within the paginated result set.

##### page_size: `int`<a id="page_size-int"></a>

Number of results to return per page.

##### search: `str`<a id="search-str"></a>

A search term.

##### type: `int`<a id="type-int"></a>

Type of the vendor. See above for possible options.

#### 🔄 Return<a id="🔄-return"></a>

[`PaginatedOptimizedVendorList`](./procurify_python_sdk/pydantic/paginated_optimized_vendor_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/vendors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.vendors.partial_update`<a id="procurifyvendorspartial_update"></a>

Partial Update Vendor

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
partial_update_response = procurify.vendors.partial_update(
    id=1,
    name="a",
    active=True,
    address_line_one="string_example",
    address_line_two="string_example",
    postal_code="string_example",
    city="string_example",
    state_province="string_example",
    country="string_example",
    phone_one="string_example",
    phone_two="string_example",
    fax="string_example",
    email=[
        "a"
    ],
    comments="string_example",
    contact="string_example",
    url="string_example",
    external_id="string_example",
    currency=1,
    payment_term_ref={
        "name": "name_example",
    },
    shipping_term_ref={
        "name": "name_example",
    },
    payment_method_ref={
        "name": "name_example",
    },
    shipping_method_ref={
        "name": "name_example",
    },
    tax=1,
    type=2,
    default_payment_method=1,
    is_1099_eligible=True,
    overall_score="48",
    is_auto_email_po_enabled=True,
    po_pdf_labels="string_example",
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

A unique integer value identifying this vendor.

##### name: `str`<a id="name-str"></a>

Name of the vendor

##### active: `bool`<a id="active-bool"></a>

##### address_line_one: `Optional[str]`<a id="address_line_one-optionalstr"></a>

First line of address

##### address_line_two: `Optional[str]`<a id="address_line_two-optionalstr"></a>

Second line of address

##### postal_code: `Optional[str]`<a id="postal_code-optionalstr"></a>

Postal or Zip code of the vendor

##### city: `Optional[str]`<a id="city-optionalstr"></a>

City of the vendor

##### state_province: `Optional[str]`<a id="state_province-optionalstr"></a>

State or Province of the vendor

##### country: `Optional[str]`<a id="country-optionalstr"></a>

Country of the vendor

##### phone_one: `Optional[str]`<a id="phone_one-optionalstr"></a>

Primary phone no. of the vendor

##### phone_two: `Optional[str]`<a id="phone_two-optionalstr"></a>

Secondary phone no. of the vendor

##### fax: `Optional[str]`<a id="fax-optionalstr"></a>

Fax no. of the vendor

##### email: [`PatchedOptimizedVendorRequestEmail`](./procurify_python_sdk/type/patched_optimized_vendor_request_email.py)<a id="email-patchedoptimizedvendorrequestemailprocurify_python_sdktypepatched_optimized_vendor_request_emailpy"></a>

##### comments: `Optional[str]`<a id="comments-optionalstr"></a>

Notes about the vendor

##### contact: `Optional[str]`<a id="contact-optionalstr"></a>

Contact person of the vendor

##### url: `Optional[str]`<a id="url-optionalstr"></a>

Website of the vendor

##### external_id: `Optional[str]`<a id="external_id-optionalstr"></a>

External id of the vendor

##### currency: `Optional[int]`<a id="currency-optionalint"></a>

##### payment_term_ref: [`PaymentTermRequestNullable`](./procurify_python_sdk/type/payment_term_request_nullable.py)<a id="payment_term_ref-paymenttermrequestnullableprocurify_python_sdktypepayment_term_request_nullablepy"></a>


##### shipping_term_ref: [`ShippingTermRequestNullable`](./procurify_python_sdk/type/shipping_term_request_nullable.py)<a id="shipping_term_ref-shippingtermrequestnullableprocurify_python_sdktypeshipping_term_request_nullablepy"></a>


##### payment_method_ref: [`PaymentMethodRequestNullable`](./procurify_python_sdk/type/payment_method_request_nullable.py)<a id="payment_method_ref-paymentmethodrequestnullableprocurify_python_sdktypepayment_method_request_nullablepy"></a>


##### shipping_method_ref: [`ShippingMethodRequestNullable`](./procurify_python_sdk/type/shipping_method_request_nullable.py)<a id="shipping_method_ref-shippingmethodrequestnullableprocurify_python_sdktypeshipping_method_request_nullablepy"></a>


##### tax: `Optional[int]`<a id="tax-optionalint"></a>

##### type: [`VendorTypeEnum`](./procurify_python_sdk/type/vendor_type_enum.py)<a id="type-vendortypeenumprocurify_python_sdktypevendor_type_enumpy"></a>

##### default_payment_method: `Optional[int]`<a id="default_payment_method-optionalint"></a>

##### is_1099_eligible: `Optional[bool]`<a id="is_1099_eligible-optionalbool"></a>

##### overall_score: `Optional[str]`<a id="overall_score-optionalstr"></a>

##### is_auto_email_po_enabled: `bool`<a id="is_auto_email_po_enabled-bool"></a>

##### po_pdf_labels: `str`<a id="po_pdf_labels-str"></a>

Placeholder for a KVStore value

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PatchedOptimizedVendorRequest`](./procurify_python_sdk/type/patched_optimized_vendor_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OptimizedVendorSerializerSingle`](./procurify_python_sdk/pydantic/optimized_vendor_serializer_single.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/vendors/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.vendors.retrieve`<a id="procurifyvendorsretrieve"></a>

Get detail of a vendor by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = procurify.vendors.retrieve(
    id=1,
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

A unique integer value identifying this vendor.

##### format: `str`<a id="format-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`VendorDetailSerializerSingleRetrieve`](./procurify_python_sdk/pydantic/vendor_detail_serializer_single_retrieve.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/vendors/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `procurify.vendors.update`<a id="procurifyvendorsupdate"></a>

Update Vendor

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = procurify.vendors.update(
    name="a",
    email=[
        "a"
    ],
    type=2,
    overall_score="48",
    id=1,
    active=True,
    address_line_one="string_example",
    address_line_two="string_example",
    postal_code="string_example",
    city="string_example",
    state_province="string_example",
    country="string_example",
    phone_one="string_example",
    phone_two="string_example",
    fax="string_example",
    comments="string_example",
    contact="string_example",
    url="string_example",
    external_id="string_example",
    currency=1,
    payment_term_ref={
        "name": "name_example",
    },
    shipping_term_ref={
        "name": "name_example",
    },
    payment_method_ref={
        "name": "name_example",
    },
    shipping_method_ref={
        "name": "name_example",
    },
    tax=1,
    default_payment_method=1,
    is_1099_eligible=True,
    is_auto_email_po_enabled=True,
    po_pdf_labels="string_example",
    format="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the vendor

##### email: [`OptimizedVendorRequestEmail`](./procurify_python_sdk/type/optimized_vendor_request_email.py)<a id="email-optimizedvendorrequestemailprocurify_python_sdktypeoptimized_vendor_request_emailpy"></a>

##### type: [`VendorTypeEnum`](./procurify_python_sdk/type/vendor_type_enum.py)<a id="type-vendortypeenumprocurify_python_sdktypevendor_type_enumpy"></a>

##### overall_score: `Optional[str]`<a id="overall_score-optionalstr"></a>

##### id: `int`<a id="id-int"></a>

A unique integer value identifying this vendor.

##### active: `bool`<a id="active-bool"></a>

##### address_line_one: `Optional[str]`<a id="address_line_one-optionalstr"></a>

First line of address

##### address_line_two: `Optional[str]`<a id="address_line_two-optionalstr"></a>

Second line of address

##### postal_code: `Optional[str]`<a id="postal_code-optionalstr"></a>

Postal or Zip code of the vendor

##### city: `Optional[str]`<a id="city-optionalstr"></a>

City of the vendor

##### state_province: `Optional[str]`<a id="state_province-optionalstr"></a>

State or Province of the vendor

##### country: `Optional[str]`<a id="country-optionalstr"></a>

Country of the vendor

##### phone_one: `Optional[str]`<a id="phone_one-optionalstr"></a>

Primary phone no. of the vendor

##### phone_two: `Optional[str]`<a id="phone_two-optionalstr"></a>

Secondary phone no. of the vendor

##### fax: `Optional[str]`<a id="fax-optionalstr"></a>

Fax no. of the vendor

##### comments: `Optional[str]`<a id="comments-optionalstr"></a>

Notes about the vendor

##### contact: `Optional[str]`<a id="contact-optionalstr"></a>

Contact person of the vendor

##### url: `Optional[str]`<a id="url-optionalstr"></a>

Website of the vendor

##### external_id: `Optional[str]`<a id="external_id-optionalstr"></a>

External id of the vendor

##### currency: `Optional[int]`<a id="currency-optionalint"></a>

##### payment_term_ref: [`PaymentTermRequestNullable`](./procurify_python_sdk/type/payment_term_request_nullable.py)<a id="payment_term_ref-paymenttermrequestnullableprocurify_python_sdktypepayment_term_request_nullablepy"></a>


##### shipping_term_ref: [`ShippingTermRequestNullable`](./procurify_python_sdk/type/shipping_term_request_nullable.py)<a id="shipping_term_ref-shippingtermrequestnullableprocurify_python_sdktypeshipping_term_request_nullablepy"></a>


##### payment_method_ref: [`PaymentMethodRequestNullable`](./procurify_python_sdk/type/payment_method_request_nullable.py)<a id="payment_method_ref-paymentmethodrequestnullableprocurify_python_sdktypepayment_method_request_nullablepy"></a>


##### shipping_method_ref: [`ShippingMethodRequestNullable`](./procurify_python_sdk/type/shipping_method_request_nullable.py)<a id="shipping_method_ref-shippingmethodrequestnullableprocurify_python_sdktypeshipping_method_request_nullablepy"></a>


##### tax: `Optional[int]`<a id="tax-optionalint"></a>

##### default_payment_method: `Optional[int]`<a id="default_payment_method-optionalint"></a>

##### is_1099_eligible: `Optional[bool]`<a id="is_1099_eligible-optionalbool"></a>

##### is_auto_email_po_enabled: `bool`<a id="is_auto_email_po_enabled-bool"></a>

##### po_pdf_labels: `str`<a id="po_pdf_labels-str"></a>

Placeholder for a KVStore value

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OptimizedVendorRequest`](./procurify_python_sdk/type/optimized_vendor_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VendorSerializerSingle`](./procurify_python_sdk/pydantic/vendor_serializer_single.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/vendors/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
