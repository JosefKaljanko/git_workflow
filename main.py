def calculate_discounted_price(price: float, discount_percent: int) -> float:
    return price * (1 - discount_percent / 100)

def main():
    print("Aplikace pro výpočet slevy.")

    price = 1000
    discount_percent = 20
    discounted_price = calculate_discounted_price(price, discount_percent)

    print(f"Cena po slevě: {discounted_price:.2f} Kč.")


if __name__ == '__main__':
    main()