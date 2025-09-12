from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

class PaypalPayment(PaymentStrategy):

    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount:.2f} through PayPal.")

class StripePayment(PaymentStrategy):

    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount:.2f} through Stripe.")

class CreditcardPayment(PaymentStrategy):

    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount:.2f} through Credit Card.")

class PaymentFactory:

    @staticmethod
    def get_payment_method(method: str) -> PaymentStrategy:
        if method == "paypal":
            return PaypalPayment()
        elif method == "stripe":
            return StripePayment()
        elif method == "creditcard":
            return CreditcardPayment()
        else:
            raise ValueError(f"Unknown payment method: {method}")
        
# Example usage
if __name__ == "__main__":
    amount = 100.0
    method = "paypal"  # This could be dynamic based on user input

    payment_method = PaymentFactory.get_payment_method(method)
    payment_method.process_payment(amount)