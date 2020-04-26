import 'dart:convert';

import 'package:hackernews_flutter/src/article.dart';
import 'package:hackernews_flutter/src/serializers.dart';

List<int> parseTopStories(jsonString) {
  final parsed = jsonDecode(jsonString);
  final listOfIds = List<int>.from(parsed);
  return listOfIds;
}

Article parseArticle(jsonString) {
  Article article =
      serializers.deserializeWith(Article.serializer, jsonDecode(jsonString));
  return article;
}
