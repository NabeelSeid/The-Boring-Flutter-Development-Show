import 'package:built_value/built_value.dart';
import 'package:built_value/serializer.dart';
import 'package:built_collection/built_collection.dart';

part 'article.g.dart';

abstract class Article implements Built<Article, ArticleBuilder> {
  int get id;
  @nullable
  bool get deleted;
  ///Type of articles
  /// "job", "story", "comment", "poll", or "pollopt".
  String get type; 
  @nullable
  String get by;
  @nullable
  int get time;
  @nullable
  String get text;
  @nullable
  bool get dead;
  @nullable
  int get parent;
  @nullable
  int get poll;
  @nullable
  BuiltList<int> get kids;
  @nullable
  String get url;
  @nullable
  int get score;
  @nullable
  String get title;
  @nullable
  BuiltList<int> get parts;
  @nullable
  int get descendants;

  Article._();
  factory Article([void Function(ArticleBuilder) updates]) = _$Article;
  static Serializer<Article> get serializer => _$articleSerializer;
}
