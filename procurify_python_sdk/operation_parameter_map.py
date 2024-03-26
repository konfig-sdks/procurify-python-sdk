operation_parameter_map = {
    '/api/v3/account-codes-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'account_type'
            },
            {
                'name': 'departments'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/account-codes-GET': {
        'parameters': [
            {
                'name': 'active'
            },
            {
                'name': 'code'
            },
            {
                'name': 'format'
            },
            {
                'name': 'is_parent'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/api/v3/account-codes/{id}-PUT': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
            {
                'name': 'id'
            },
            {
                'name': 'account_type'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/accounts-GET': {
        'parameters': [
            {
                'name': 'account_code'
            },
            {
                'name': 'active'
            },
            {
                'name': 'department'
            },
            {
                'name': 'departments'
            },
            {
                'name': 'format'
            },
            {
                'name': 'id'
            },
            {
                'name': 'in_effect'
            },
            {
                'name': 'locations'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'search'
            },
            {
                'name': 'with_expired_budgets'
            },
        ]
    },
    '/api/v2/ap/bills/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/ap/bills-GET': {
        'parameters': [
            {
                'name': 'approver'
            },
            {
                'name': 'contract'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'due_date_0'
            },
            {
                'name': 'due_date_1'
            },
            {
                'name': 'exclude_bill_group_ids'
            },
            {
                'name': 'exclude_expense_bills'
            },
            {
                'name': 'expense'
            },
            {
                'name': 'format'
            },
            {
                'name': 'gl_post_date_0'
            },
            {
                'name': 'gl_post_date_1'
            },
            {
                'name': 'group'
            },
            {
                'name': 'has_payment'
            },
            {
                'name': 'has_posting_date'
            },
            {
                'name': 'include_bill_group_ids'
            },
            {
                'name': 'invoice_date_0'
            },
            {
                'name': 'invoice_date_1'
            },
            {
                'name': 'is_exported'
            },
            {
                'name': 'last_export_date_0'
            },
            {
                'name': 'last_export_date_1'
            },
            {
                'name': 'last_export_user'
            },
            {
                'name': 'last_modified_datetime_0'
            },
            {
                'name': 'last_modified_datetime_1'
            },
            {
                'name': 'modified_date_0'
            },
            {
                'name': 'modified_date_1'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'search'
            },
            {
                'name': 'submitted_date_0'
            },
            {
                'name': 'submitted_date_1'
            },
            {
                'name': 'sync_status'
            },
            {
                'name': 'sync_status_v2'
            },
            {
                'name': 'type'
            },
            {
                'name': 'user'
            },
            {
                'name': 'vendor'
            },
        ]
    },
    '/api/v2/ap/company-payment-methods-GET': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'format'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'search'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v2/ap/company-payment-methods-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'gl_code'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v2/ap/vendor-payment-methods-POST': {
        'parameters': [
            {
                'name': 'vendor'
            },
            {
                'name': 'data'
            },
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v2/ap/payments-GET': {
        'parameters': [
            {
                'name': 'approver'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'format'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'payment_date_0'
            },
            {
                'name': 'payment_date_1'
            },
            {
                'name': 'payment_method__type'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/api/v2/ap/items-GET': {
        'parameters': [
            {
                'name': 'bill'
            },
            {
                'name': 'bill_uuid'
            },
            {
                'name': 'billed'
            },
            {
                'name': 'budget'
            },
            {
                'name': 'created_at_0'
            },
            {
                'name': 'created_at_1'
            },
            {
                'name': 'department'
            },
            {
                'name': 'exclude'
            },
            {
                'name': 'format'
            },
            {
                'name': 'location'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'received_on_0'
            },
            {
                'name': 'received_on_1'
            },
            {
                'name': 'reimburse'
            },
            {
                'name': 'requester'
            },
            {
                'name': 'search'
            },
            {
                'name': 'vendor'
            },
        ]
    },
    '/api/v2/ap/payments/{id}/approver-choices-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v2/ap/vendor-payment-methods-GET': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'format'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'search'
            },
            {
                'name': 'type'
            },
            {
                'name': 'vendor'
            },
        ]
    },
    '/api/v3/catalog-bundles-GET': {
        'parameters': [
            {
                'name': 'format'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/api/v3/catalog-items-GET': {
        'parameters': [
            {
                'name': 'bundle'
            },
            {
                'name': 'department'
            },
            {
                'name': 'format'
            },
            {
                'name': 'internalSKU'
            },
            {
                'name': 'location'
            },
            {
                'name': 'max_price'
            },
            {
                'name': 'min_price'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'pref_vendor'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/api/v3/catalog-items-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'custom_fields'
            },
            {
                'name': 'description'
            },
            {
                'name': 'id'
            },
            {
                'name': 'image'
            },
            {
                'name': 'unitType'
            },
            {
                'name': 'pref_vendor'
            },
            {
                'name': 'account_code'
            },
            {
                'name': 'internalSKU'
            },
            {
                'name': 'product_url'
            },
            {
                'name': 'price'
            },
            {
                'name': 'rfo_lock'
            },
            {
                'name': 'departments'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/catalog-items/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'custom_fields'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'id'
            },
            {
                'name': 'image'
            },
            {
                'name': 'unitType'
            },
            {
                'name': 'pref_vendor'
            },
            {
                'name': 'account_code'
            },
            {
                'name': 'internalSKU'
            },
            {
                'name': 'product_url'
            },
            {
                'name': 'price'
            },
            {
                'name': 'rfo_lock'
            },
            {
                'name': 'departments'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v2/currencies-GET': {
        'parameters': [
            {
                'name': 'active'
            },
            {
                'name': 'base'
            },
            {
                'name': 'description'
            },
            {
                'name': 'format'
            },
            {
                'name': 'name'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'rate'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/api/v3/custom-fields/order-items-GET': {
        'parameters': [
            {
                'name': 'field_type'
            },
            {
                'name': 'format'
            },
            {
                'name': 'meta__is_active'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/api/v3/custom-fields/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'field_type'
            },
            {
                'name': 'id'
            },
            {
                'name': 'default_value'
            },
            {
                'name': 'is_required'
            },
            {
                'name': 'field_choices'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/departments-POST': {
        'parameters': [
            {
                'name': 'branch'
            },
            {
                'name': 'name'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'punchout_email'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/departments-GET': {
        'parameters': [
            {
                'name': 'branch'
            },
            {
                'name': 'format'
            },
            {
                'name': 'include_is_active_for_account_code'
            },
            {
                'name': 'location_perm_override'
            },
            {
                'name': 'locations'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'permission'
            },
            {
                'name': 'requestable'
            },
            {
                'name': 'search'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/api/v3/departments/{id}-PUT': {
        'parameters': [
            {
                'name': 'branch'
            },
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'punchout_email'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v2/locations-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'phoneOne'
            },
            {
                'name': 'primary_billing_address'
            },
            {
                'name': 'primary_shipping_address'
            },
            {
                'name': 'shipping_addresses'
            },
            {
                'name': 'url'
            },
            {
                'name': 'logo'
            },
            {
                'name': 'fax'
            },
            {
                'name': 'email'
            },
            {
                'name': 'language'
            },
            {
                'name': 'locationTimezone'
            },
            {
                'name': 'active'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v2/locations-GET': {
        'parameters': [
            {
                'name': 'active'
            },
            {
                'name': 'format'
            },
            {
                'name': 'headquarter'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/api/v2/locations/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/oauth/token-POST': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'audience'
            },
            {
                'name': 'grant_type'
            },
        ]
    },
    '/api/v3/order-items-GET': {
        'parameters': [
            {
                'name': 'account'
            },
            {
                'name': 'account_code'
            },
            {
                'name': 'active'
            },
            {
                'name': 'approved_datetime_0'
            },
            {
                'name': 'approved_datetime_1'
            },
            {
                'name': 'approved_price'
            },
            {
                'name': 'approved_quantity'
            },
            {
                'name': 'approver'
            },
            {
                'name': 'approver_id'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'catalog'
            },
            {
                'name': 'catalog_item'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'department'
            },
            {
                'name': 'departments'
            },
            {
                'name': 'exclude'
            },
            {
                'name': 'exclude_punchout'
            },
            {
                'name': 'format'
            },
            {
                'name': 'fulfilment_status'
            },
            {
                'name': 'is_purchased'
            },
            {
                'name': 'is_recurring'
            },
            {
                'name': 'last_changed_by'
            },
            {
                'name': 'last_modified_0'
            },
            {
                'name': 'last_modified_1'
            },
            {
                'name': 'lineComment'
            },
            {
                'name': 'location'
            },
            {
                'name': 'locations'
            },
            {
                'name': 'name'
            },
            {
                'name': 'num'
            },
            {
                'name': 'orderNum'
            },
            {
                'name': 'orderNum__status'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'order_created_date_0'
            },
            {
                'name': 'order_created_date_1'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'po_created_date_0'
            },
            {
                'name': 'po_created_date_1'
            },
            {
                'name': 'po_vendor'
            },
            {
                'name': 'pref_vendor'
            },
            {
                'name': 'price'
            },
            {
                'name': 'purchase_agreement'
            },
            {
                'name': 'purchased_date_0'
            },
            {
                'name': 'purchased_date_1'
            },
            {
                'name': 'purchaser'
            },
            {
                'name': 'quantity'
            },
            {
                'name': 'receivedFailQty'
            },
            {
                'name': 'receivedPassQty'
            },
            {
                'name': 'requester'
            },
            {
                'name': 'search'
            },
            {
                'name': 'sku'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'unit'
            },
        ]
    },
    '/api/v3/permissions/groups-GET': {
        'parameters': [
            {
                'name': 'format'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'permission'
            },
            {
                'name': 'search'
            },
            {
                'name': 'type'
            },
            {
                'name': 'user'
            },
            {
                'name': 'userprofile'
            },
        ]
    },
    '/api/v3/permissions-GET': {
        'parameters': [
            {
                'name': 'format'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/api/v3/purchase-orders/{procurify_PO}/close-POST': {
        'parameters': [
            {
                'name': 'procurify_PO'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v2/purchase_orders/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v2/purchase_orders/{role}/{status}-GET': {
        'parameters': [
            {
                'name': 'role'
            },
            {
                'name': 'status'
            },
            {
                'name': 'contract'
            },
            {
                'name': 'date_0'
            },
            {
                'name': 'date_1'
            },
            {
                'name': 'expiry_date_0'
            },
            {
                'name': 'expiry_date_1'
            },
            {
                'name': 'has_blanket_order_items'
            },
            {
                'name': 'modified_date_0'
            },
            {
                'name': 'modified_date_1'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'pref_vendor'
            },
            {
                'name': 'promise_date_0'
            },
            {
                'name': 'promise_date_1'
            },
        ]
    },
    '/api/v3/purchase-orders/{procurify_PO}/reopen-POST': {
        'parameters': [
            {
                'name': 'procurify_PO'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v2/purchase_order/revise/{procurify_PO}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'order_items'
            },
            {
                'name': 'buyer_name'
            },
            {
                'name': 'buyer_contact'
            },
            {
                'name': 'buyer_addressLineOne'
            },
            {
                'name': 'buyer_postalCode'
            },
            {
                'name': 'buyer_city'
            },
            {
                'name': 'buyer_country'
            },
            {
                'name': 'buyer_address'
            },
            {
                'name': 'receiver_name'
            },
            {
                'name': 'receiver_contact'
            },
            {
                'name': 'receiver_addressLineOne'
            },
            {
                'name': 'receiver_postalCode'
            },
            {
                'name': 'receiver_city'
            },
            {
                'name': 'receiver_country'
            },
            {
                'name': 'receiver_address'
            },
            {
                'name': 'promise_date'
            },
            {
                'name': 'discount'
            },
            {
                'name': 'tax'
            },
            {
                'name': 'procurify_PO'
            },
            {
                'name': 'custom_fields'
            },
            {
                'name': 'PO_Num'
            },
            {
                'name': 'buyer_state_province'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'receiver_state_province'
            },
            {
                'name': 'freight'
            },
            {
                'name': 'other'
            },
            {
                'name': 'disclaimer_description'
            },
            {
                'name': 'disclaimer_text'
            },
            {
                'name': 'payment_term_ref'
            },
            {
                'name': 'shipping_term_ref'
            },
            {
                'name': 'payment_method_ref'
            },
            {
                'name': 'shipping_method_ref'
            },
            {
                'name': 'creditcard'
            },
            {
                'name': 'expiry_date'
            },
            {
                'name': 'contract'
            },
            {
                'name': 'confirm_duplicate_external_po_number'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/purchase-orders/{procurify_PO}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'order_items'
            },
            {
                'name': 'buyer_name'
            },
            {
                'name': 'buyer_contact'
            },
            {
                'name': 'buyer_addressLineOne'
            },
            {
                'name': 'buyer_postalCode'
            },
            {
                'name': 'buyer_city'
            },
            {
                'name': 'buyer_country'
            },
            {
                'name': 'buyer_address'
            },
            {
                'name': 'receiver_name'
            },
            {
                'name': 'receiver_contact'
            },
            {
                'name': 'receiver_addressLineOne'
            },
            {
                'name': 'receiver_postalCode'
            },
            {
                'name': 'receiver_city'
            },
            {
                'name': 'receiver_country'
            },
            {
                'name': 'receiver_address'
            },
            {
                'name': 'promise_date'
            },
            {
                'name': 'discount'
            },
            {
                'name': 'tax'
            },
            {
                'name': 'procurify_PO'
            },
            {
                'name': 'custom_fields'
            },
            {
                'name': 'PO_Num'
            },
            {
                'name': 'buyer_state_province'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'receiver_state_province'
            },
            {
                'name': 'freight'
            },
            {
                'name': 'other'
            },
            {
                'name': 'disclaimer_description'
            },
            {
                'name': 'disclaimer_text'
            },
            {
                'name': 'payment_term_ref'
            },
            {
                'name': 'shipping_term_ref'
            },
            {
                'name': 'payment_method_ref'
            },
            {
                'name': 'shipping_method_ref'
            },
            {
                'name': 'creditcard'
            },
            {
                'name': 'expiry_date'
            },
            {
                'name': 'contract'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/purchase-orders/billing-history-GET': {
        'parameters': [
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/requisitions-POST': {
        'parameters': [
            {
                'name': 'required_date'
            },
            {
                'name': 'location_name'
            },
            {
                'name': 'department_name'
            },
            {
                'name': 'line_items'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v2/global/order_items-GET': {
        'parameters': [
            {
                'name': 'account'
            },
            {
                'name': 'account_code'
            },
            {
                'name': 'active'
            },
            {
                'name': 'approved_datetime_0'
            },
            {
                'name': 'approved_datetime_1'
            },
            {
                'name': 'approved_price'
            },
            {
                'name': 'approved_quantity'
            },
            {
                'name': 'approver'
            },
            {
                'name': 'approver_id'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'catalog'
            },
            {
                'name': 'catalog_item'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'department'
            },
            {
                'name': 'departments'
            },
            {
                'name': 'exclude'
            },
            {
                'name': 'exclude_punchout'
            },
            {
                'name': 'format'
            },
            {
                'name': 'fulfilment_status'
            },
            {
                'name': 'is_purchased'
            },
            {
                'name': 'is_recurring'
            },
            {
                'name': 'last_changed_by'
            },
            {
                'name': 'last_modified_0'
            },
            {
                'name': 'last_modified_1'
            },
            {
                'name': 'lineComment'
            },
            {
                'name': 'location'
            },
            {
                'name': 'locations'
            },
            {
                'name': 'name'
            },
            {
                'name': 'num'
            },
            {
                'name': 'orderNum'
            },
            {
                'name': 'orderNum__status'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'order_created_date_0'
            },
            {
                'name': 'order_created_date_1'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'po_created_date_0'
            },
            {
                'name': 'po_created_date_1'
            },
            {
                'name': 'po_vendor'
            },
            {
                'name': 'pref_vendor'
            },
            {
                'name': 'price'
            },
            {
                'name': 'purchase_agreement'
            },
            {
                'name': 'purchased_date_0'
            },
            {
                'name': 'purchased_date_1'
            },
            {
                'name': 'purchaser'
            },
            {
                'name': 'quantity'
            },
            {
                'name': 'receivedFailQty'
            },
            {
                'name': 'receivedPassQty'
            },
            {
                'name': 'requester'
            },
            {
                'name': 'search'
            },
            {
                'name': 'sku'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'unit'
            },
        ]
    },
    '/api/v2/global/orders-GET': {
        'parameters': [
            {
                'name': 'branch'
            },
            {
                'name': 'dateRequired'
            },
            {
                'name': 'date_0'
            },
            {
                'name': 'date_1'
            },
            {
                'name': 'department'
            },
            {
                'name': 'format'
            },
            {
                'name': 'has_blanket_order_items'
            },
            {
                'name': 'is_punchout'
            },
            {
                'name': 'lineCount'
            },
            {
                'name': 'location'
            },
            {
                'name': 'modified_date_0'
            },
            {
                'name': 'modified_date_1'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'required_date_0'
            },
            {
                'name': 'required_date_1'
            },
            {
                'name': 'search'
            },
            {
                'name': 'status'
            },
            {
                'name': 'totalPrice'
            },
        ]
    },
    '/api/v3/users-POST': {
        'parameters': [
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/users/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/users/me-GET': {
        'parameters': [
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/users-GET': {
        'parameters': [
            {
                'name': 'format'
            },
            {
                'name': 'is_active'
            },
            {
                'name': 'location'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'pending_invite'
            },
            {
                'name': 'permission'
            },
            {
                'name': 'role'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/api/v3/users/{id}-PUT': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'location'
            },
            {
                'name': 'department'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'user'
            },
            {
                'name': 'position'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'profile_image'
            },
            {
                'name': 'is_sso_enabled'
            },
            {
                'name': 'mark_for_skip'
            },
            {
                'name': 'mark_for_delete'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/vendors-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'type'
            },
            {
                'name': 'overall_score'
            },
            {
                'name': 'active'
            },
            {
                'name': 'addressLineOne'
            },
            {
                'name': 'addressLineTwo'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state_province'
            },
            {
                'name': 'country'
            },
            {
                'name': 'phoneOne'
            },
            {
                'name': 'phoneTwo'
            },
            {
                'name': 'fax'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'contact'
            },
            {
                'name': 'url'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'payment_term_ref'
            },
            {
                'name': 'shipping_term_ref'
            },
            {
                'name': 'payment_method_ref'
            },
            {
                'name': 'shipping_method_ref'
            },
            {
                'name': 'tax'
            },
            {
                'name': 'default_payment_method'
            },
            {
                'name': 'is_1099_eligible'
            },
            {
                'name': 'is_auto_email_po_enabled'
            },
            {
                'name': 'po_pdf_labels'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/vendors-GET': {
        'parameters': [
            {
                'name': 'vendor_group'
            },
            {
                'name': 'exclude_other'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'format'
            },
            {
                'name': 'name'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'search'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v3/vendors/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'active'
            },
            {
                'name': 'addressLineOne'
            },
            {
                'name': 'addressLineTwo'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state_province'
            },
            {
                'name': 'country'
            },
            {
                'name': 'phoneOne'
            },
            {
                'name': 'phoneTwo'
            },
            {
                'name': 'fax'
            },
            {
                'name': 'email'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'contact'
            },
            {
                'name': 'url'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'payment_term_ref'
            },
            {
                'name': 'shipping_term_ref'
            },
            {
                'name': 'payment_method_ref'
            },
            {
                'name': 'shipping_method_ref'
            },
            {
                'name': 'tax'
            },
            {
                'name': 'type'
            },
            {
                'name': 'default_payment_method'
            },
            {
                'name': 'is_1099_eligible'
            },
            {
                'name': 'overall_score'
            },
            {
                'name': 'is_auto_email_po_enabled'
            },
            {
                'name': 'po_pdf_labels'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/vendors/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/api/v3/vendors/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'type'
            },
            {
                'name': 'overall_score'
            },
            {
                'name': 'id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'addressLineOne'
            },
            {
                'name': 'addressLineTwo'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state_province'
            },
            {
                'name': 'country'
            },
            {
                'name': 'phoneOne'
            },
            {
                'name': 'phoneTwo'
            },
            {
                'name': 'fax'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'contact'
            },
            {
                'name': 'url'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'payment_term_ref'
            },
            {
                'name': 'shipping_term_ref'
            },
            {
                'name': 'payment_method_ref'
            },
            {
                'name': 'shipping_method_ref'
            },
            {
                'name': 'tax'
            },
            {
                'name': 'default_payment_method'
            },
            {
                'name': 'is_1099_eligible'
            },
            {
                'name': 'is_auto_email_po_enabled'
            },
            {
                'name': 'po_pdf_labels'
            },
            {
                'name': 'format'
            },
        ]
    },
};