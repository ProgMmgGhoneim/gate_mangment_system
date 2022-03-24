from rest_framework import serializers


class ReportSerializer(serializers.Serializer):
    REPORT_TYPE = (
        ("CAR", "CAR"),
        ("VISITOR", "VISITOR"),
        ("GATE", "GATE"),
        ("VisitorTrace", "VisitorTrace"),
    )
    report_type = serializers.ChoiceField(
        choices=REPORT_TYPE)
    start_at = serializers.DateTimeField()
    end_at = serializers.DateTimeField()

    def to_representation(self, instance):
        representation = super(ReportSerializer, self).to_representation(instance)
        representation['created_at'] = instance.created_at.strftime("<your format string>")
        return representation