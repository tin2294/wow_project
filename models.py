class Order(models.Model):
    """ Order """
    oid = models.CharField(verbose_name="Order number", max_length=64)
    title = models.CharField(verbose_name="Name", max_length=32)
    price = models.IntegerField(verbose_name="Price")

    status_choices = (
        (1, "To be paid"),
        (2, "Paid"),
    )
    status = models.SmallIntegerField(verbose_name="status_choices", choices=status_choices, default=1)
    # admin_id
    admin = models.ForeignKey(verbose_name="Manager", to="Admin", on_delete=models.CASCADE)