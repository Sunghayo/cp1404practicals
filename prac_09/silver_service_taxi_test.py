"""
CP1404/CP5632 Practical
SilverServiceTaxi Test Program
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    # Create a SilverServiceTaxi with fanciness of 2
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(18)

    # Test initial values
    assert taxi.flagfall == 4.50
    assert taxi.price_per_km == Taxi.price_per_km * 2  # Base price * fanciness

    # Test the fare calculation
    # 18km travelled at $2.46/km ($1.23 * 2) plus $4.50 flagfall = $48.78
    fare = taxi.get_fare()
    assert round(fare, 2) == 48.78, f"Expected $48.78, got ${fare:.2f}"

    # Test the string formatting
    taxi_str = str(taxi)
    assert "Hummer" in taxi_str
    assert "plus flagfall of $4.50" in taxi_str

    print("All tests passed!")

    # Display taxi details and fare for verification
    print(taxi)
    print(f"Fare: ${fare:.2f}")


main()