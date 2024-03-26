import typing_extensions

from procurify_python_sdk.apis.tags import TagValues
from procurify_python_sdk.apis.tags.ap_api import ApApi
from procurify_python_sdk.apis.tags.purchase_orders_api import PurchaseOrdersApi
from procurify_python_sdk.apis.tags.users_api import UsersApi
from procurify_python_sdk.apis.tags.vendors_api import VendorsApi
from procurify_python_sdk.apis.tags.catalog_api import CatalogApi
from procurify_python_sdk.apis.tags.locations_api import LocationsApi
from procurify_python_sdk.apis.tags.departments_api import DepartmentsApi
from procurify_python_sdk.apis.tags.account_codes_api import AccountCodesApi
from procurify_python_sdk.apis.tags.requisitions_api import RequisitionsApi
from procurify_python_sdk.apis.tags.permissions_api import PermissionsApi
from procurify_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from procurify_python_sdk.apis.tags.oauth_api import OauthApi
from procurify_python_sdk.apis.tags.accounts_api import AccountsApi
from procurify_python_sdk.apis.tags.currencies_api import CurrenciesApi
from procurify_python_sdk.apis.tags.order_items_api import OrderItemsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AP: ApApi,
        TagValues.PURCHASEORDERS: PurchaseOrdersApi,
        TagValues.USERS: UsersApi,
        TagValues.VENDORS: VendorsApi,
        TagValues.CATALOG: CatalogApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.ACCOUNTCODES: AccountCodesApi,
        TagValues.REQUISITIONS: RequisitionsApi,
        TagValues.PERMISSIONS: PermissionsApi,
        TagValues.CUSTOMFIELDS: CustomFieldsApi,
        TagValues.OAUTH: OauthApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.CURRENCIES: CurrenciesApi,
        TagValues.ORDERITEMS: OrderItemsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AP: ApApi,
        TagValues.PURCHASEORDERS: PurchaseOrdersApi,
        TagValues.USERS: UsersApi,
        TagValues.VENDORS: VendorsApi,
        TagValues.CATALOG: CatalogApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.ACCOUNTCODES: AccountCodesApi,
        TagValues.REQUISITIONS: RequisitionsApi,
        TagValues.PERMISSIONS: PermissionsApi,
        TagValues.CUSTOMFIELDS: CustomFieldsApi,
        TagValues.OAUTH: OauthApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.CURRENCIES: CurrenciesApi,
        TagValues.ORDERITEMS: OrderItemsApi,
    }
)
