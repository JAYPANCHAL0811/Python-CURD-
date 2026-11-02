tvshop_list = []
next_id = 1


def add_tv(brand, model, screen_size, price, status="Available"):
    """Create a new TV record and add it to the list."""
    global next_id

    tv = {
        "id": next_id,
        "brand": brand,
        "model": model,
        "screen_size": screen_size,
        "price": price,
        "status": status
    }

    tvshop_list.append(tv)
    next_id += 1

    print(f"\nTV '{brand} {model}' added successfully with ID {tv['id']}.")


def view_tvs():
    """Display all TV records."""
    if not tvshop_list:
        print("\nNo TV records found.")
        return

    print("\n----- TV Shop Inventory -----")
    for tv in tvshop_list:
        print(f"ID: {tv['id']} | Brand: {tv['brand']} | Model: {tv['model']} | "
              f"Screen Size: {tv['screen_size']} | Price: {tv['price']} | "
              f"Status: {tv['status']}")
    print("-----------------------------")


def search_tv(tv_id):
    """Find and return a single TV record by ID."""
    for tv in tvshop_list:
        if tv["id"] == tv_id:
            return tv
    return None


def update_tv(tv_id, brand=None, model=None, screen_size=None, price=None, status=None):
    """Update an existing TV record."""
    tv = search_tv(tv_id)

    if tv is None:
        print(f"\nNo TV found with ID {tv_id}.")
        return

    if brand:
        tv["brand"] = brand
    if model:
        tv["model"] = model
    if screen_size:
        tv["screen_size"] = screen_size
    if price:
        tv["price"] = price
    if status:
        tv["status"] = status

    print(f"\nTV ID {tv_id} updated successfully.")


def delete_tv(tv_id):
    """Delete a TV record by ID."""
    tv = search_tv(tv_id)

    if tv is None:
        print(f"\nNo TV found with ID {tv_id}.")
        return

    tvshop_list.remove(tv)
    print(f"\nTV ID {tv_id} deleted successfully.")
