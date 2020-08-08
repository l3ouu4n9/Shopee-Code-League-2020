## File description

- delivery_orders_march.csv - Contains all the relevant information for orders delivered in the month of March.
- SLA_matrix.xlsx - Contains the Service Level Agreements for the different routes.

### Data fields for delivery_orders_march

- orderid- Each orderid represents a distinct transaction on Shopee
- pick - Pick Up Time, which is defined as the time (represented by epoch time) when the 3PL picks up the parcel and begins to process for delivery
- 1st_deliver_attempt - Time (represented by epoch time) when 3PL first attempts a delivery.
- 2nd_deliver_attempt - Time (represented by epoch time) when 3PL attempts a delivery again after the 1st attempt has failed. Orders which were successfully delivered the 1st time will not have a 2nd attempt
- buyeraddress - buyer's address (Destination)
- selleraddress- seller's address (Origin)