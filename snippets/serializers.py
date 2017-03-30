# coding=utf-8
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=100, required=False, allow_blank=True)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    # 只有反序列化时才需要验证
    # 调用Serializer的save方法时，有可能调用create也有可能调用update，这取决于实例是否已经存在。如何判定实例是否已经存在？
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()  # instance实例是什么类型？为何有save()方法？
        return instance

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlight')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail',
                                                   read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
