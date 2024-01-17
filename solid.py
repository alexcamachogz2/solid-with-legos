# Single Responsibility Principle
class Order:
    def __init__(self, customer, details):
        self.customer = customer
        self.details = details

    def describe_order(self):
        return f"Order for {self.customer}: {self.details}"

# Open/Closed Principle
class PaymentProcessor:
    def process_payment(self, order, payment):
        pass

class CardPayment(PaymentProcessor):
    def process_payment(self, order, payment):
        # Process card payment
        pass

class CashPayment(PaymentProcessor):
    def process_payment(self, order, payment):
        # Process cash payment
        pass

# Liskov Substitution Principle
def finalize_order(processor, order, payment):
    processor.process_payment(order, payment)
    return "Order finalized"

# Interface Segregation Principle
class Notifier:
    def send_notification(self, message):
        pass

class EmailNotifier(Notifier):
    def send_notification(self, message):
        # Send notification via email
        pass

class SMSNotifier(Notifier):
    def send_notification(self, message):
        # Send notification via SMS
        pass

# Dependency Inversion Principle
class OrderManager:
    def __init__(self, processor: PaymentProcessor, notifier: Notifier):
        self.processor = processor
        self.notifier = notifier

    def process_order(self, order, payment):
        result = finalize_order(self.processor, order, payment)
        self.notifier.send_notification(f"Notification: {result}")

# Using the classes
order = Order("John Doe", "1 Margherita pizza, 2 Cokes")
payment_processor = CardPayment()
notifier = EmailNotifier()
manager = OrderManager(payment_processor, notifier)

manager.process_order(order, "Payment with Visa card")
