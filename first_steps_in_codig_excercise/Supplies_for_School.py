pkg_pens = int(input())
pkg_markers = int(input())
detergent_leters = int(input())
discount_percentage = int(input())
price_pkg_pens = pkg_pens * 5.80
price_pkg_markers = pkg_markers * 7.2
price_detergent = detergent_leters * 1.2
price_all = price_pkg_pens + price_pkg_markers + price_detergent
price_discounted = price_all - (price_all * discount_percentage / 100)
print(price_discounted)