def trip_price ( dist_miles,mpg,price,loc_from="A",loc_to="B"):
    total= dist_miles*price / mpg


    print(f"Viaje de  {loc_from} a {loc_to} = ${total}")

trip_price(409, 35, 3.8)
