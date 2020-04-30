import 'package:rxdart/rxdart.dart';
import 'package:http/http.dart' as http;

import 'package:hackernews_flutter/src/article.dart';
import 'package:hackernews_flutter/src/json_parsing.dart';

class HackerNewsBloc {
  final _articlesSubject = BehaviorSubject<List<Article>>();

  var _articles = <Article>[];

  List<int> _ids = [
    22999738,
    22998668,
    23000628,
    22997193,
    22994420,
    22999096,
    22998423,
    22999128,
    22996374
  ];

  HackerNewsBloc() {
    updateArticles().then((n) {
      _articlesSubject.add(_articles);
      _articlesSubject.close();
    });
  }

  Stream<List<Article>> get articles => _articlesSubject.stream;

  Future<Article> _getArticle(int id) async {
    final storyUrl = 'https://hacker-news.firebaseio.com/v0/item/${id}.json';
    final storyRes = await http.get(storyUrl);
    return parseArticle(storyRes.body);
  }

  Future<Null> updateArticles() async {
    final futureArticles = _ids.map((id) => _getArticle(id));
    final articles = await Future.wait(futureArticles);
    _articles = articles;
  }
}
