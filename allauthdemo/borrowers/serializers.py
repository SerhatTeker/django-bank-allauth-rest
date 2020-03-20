from rest_framework import serializers

from .models import Borrower
from .models import Invoice


class BorrowerSerializer(serializers.ModelSerializer):
    open_invoices_count = serializers.ReadOnlyField()
    overdue_invoices_count = serializers.ReadOnlyField()
    paid_invoices_count = serializers.ReadOnlyField()

    def create(self, validated_data):
        user = self.context["request"].user
        instance = Borrower(admin_creator=user, **validated_data)
        instance.save()

        return instance

    class Meta:
        model = Borrower
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "iban",
            "open_invoices_count",
            "overdue_invoices_count",
            "paid_invoices_count",
        )


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"
