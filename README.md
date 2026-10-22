# mansmade-media

Product photography for **MansMade Legacy Co.**, handcrafted woodworking, CNC fabrication and 3D-printed goods made in Oklahoma.

This repository stages web-optimized product images so they can be imported into the MansMade Shopify store and displayed on [mansmadelegacyco.com](https://mansmadelegacyco.com). Shopify keeps its own copy of each image once a listing is created.

## Layout

```
products/
  <product-handle>/
    <product-handle>-01.jpg   main photo
    <product-handle>-02.jpg   additional angles and details
brand/
  mansmade-logo-on-dark.png   logo for dark backgrounds (store header)
  mansmade-logo-on-light.png  logo for light backgrounds (emails, checkout)
tools/
  prepare_photos.py           resizes, orients and strips metadata
```

The product handle matches the product's handle in Shopify, for example `purpleheart-maple-cutting-board`.

## Photo standards

- JPEG, sRGB, longest side up to 2400 px.
- Upright orientation applied.
- **All metadata removed** before upload, including GPS location, camera details and timestamps.

## Copyright

All images © MansMade Legacy Co. All rights reserved. These photos are published here only to supply the MansMade store and website. No license is granted to copy, reuse, modify or redistribute them.
