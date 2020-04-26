import 'package:built_value/built_value.dart';
import 'package:built_value/serializer.dart';

part 'article.g.dart';

abstract class Article implements Built<Article, ArticleBuilder> {
  String get title;
  String get url;
  String get by;
  int get time;
  int get score;

  Article._();
  factory Article([void Function(ArticleBuilder) updates]) = _$Article;
  static Serializer<Article> get serializer => _$articleSerializer;
}