
{
'international_delivery_mode' : False, # todos nulos 'none'
'title' : True,
'site_id' : True,
'shipping' : ['local_pick_up','free_methods','free_shipping','tags','methods','mode','dimensions'],
'descriptions':["{'id': 'MLA4695330653-912855983'}"],
'condition': False,
'base_price':True,
'variations':True, #posible uso',
'accepts_mercadopago': True,
'stop_time':True, # formato raro
'currency_id':True, # si es dolar o peso {'ARS', 'USD'}
'listing_source':False, # todos nulos {''}
'date_created':True, # Fecha y hora de creacion
'seller_id': True, # Vendedor
'id': True, # id del producto
'attributes': True, # formato raro
'automatic_relist':True,# buileano {False, True}
'category_id':True,
'listing_type_id':True,# caracteristicas {'bronze','free','gold', 'gold_premium','gold_pro','gold_special', 'silver'}
'coverage_areas': False, # todos nulos []
'video_id': True,# Muchos nulos pero puede serr buleano (original colocan video)
'buying_mode':True,#metodo de venta {'auction', 'buy_it_now', 'classified'}
'last_updated':True,# datetime 
'start_time':True,# formato raro
'warranty':True,# bueano (los originales tienen garantia)
'parent_item_id':True, # no todos tienen este id
'differential_pricing':False, # Todos nulos
'initial_quantity':True,
'secure_thumbnail':True, # usarse como buleano si tiene o no imagen
'subtitle':False, # todos Nulos {None}
'price':True,
'status':True,# {'active', 'closed', 'not_yet_active', 'paused'}
'thumbnail':True, # usarse como buleano si tiene o no imagen
'pictures':True, # usarse como buleano si tiene o no imagen
'tags':True, # es una lista
'original_price':True,# puede ser una buena opcion
'official_store_id':True,# puede ser una buena opcion
'sold_quantity':True,
'non_mercado_pago_payment_methods':True,# formato raro puede ser una buena opcion
'sub_status': True, # habla de suspendidos
'seller_address':True,# formato raro puede ser buena opcion
'catalog_product_id':True, # Tiene muchos nulos
'permalink':True, # usarse como buleano si tiene o no imagen
'available_quantity':True, # puede ser
'deal_ids': True # tiene un lista

}