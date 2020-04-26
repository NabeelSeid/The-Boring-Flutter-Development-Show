// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'article.dart';

// **************************************************************************
// BuiltValueGenerator
// **************************************************************************

Serializer<Article> _$articleSerializer = new _$ArticleSerializer();

class _$ArticleSerializer implements StructuredSerializer<Article> {
  @override
  final Iterable<Type> types = const [Article, _$Article];
  @override
  final String wireName = 'Article';

  @override
  Iterable<Object> serialize(Serializers serializers, Article object,
      {FullType specifiedType = FullType.unspecified}) {
    final result = <Object>[
      'title',
      serializers.serialize(object.title,
          specifiedType: const FullType(String)),
      'url',
      serializers.serialize(object.url, specifiedType: const FullType(String)),
      'by',
      serializers.serialize(object.by, specifiedType: const FullType(String)),
      'time',
      serializers.serialize(object.time, specifiedType: const FullType(int)),
      'score',
      serializers.serialize(object.score, specifiedType: const FullType(int)),
    ];

    return result;
  }

  @override
  Article deserialize(Serializers serializers, Iterable<Object> serialized,
      {FullType specifiedType = FullType.unspecified}) {
    final result = new ArticleBuilder();

    final iterator = serialized.iterator;
    while (iterator.moveNext()) {
      final key = iterator.current as String;
      iterator.moveNext();
      final dynamic value = iterator.current;
      switch (key) {
        case 'title':
          result.title = serializers.deserialize(value,
              specifiedType: const FullType(String)) as String;
          break;
        case 'url':
          result.url = serializers.deserialize(value,
              specifiedType: const FullType(String)) as String;
          break;
        case 'by':
          result.by = serializers.deserialize(value,
              specifiedType: const FullType(String)) as String;
          break;
        case 'time':
          result.time = serializers.deserialize(value,
              specifiedType: const FullType(int)) as int;
          break;
        case 'score':
          result.score = serializers.deserialize(value,
              specifiedType: const FullType(int)) as int;
          break;
      }
    }

    return result.build();
  }
}

class _$Article extends Article {
  @override
  final String title;
  @override
  final String url;
  @override
  final String by;
  @override
  final int time;
  @override
  final int score;

  factory _$Article([void Function(ArticleBuilder) updates]) =>
      (new ArticleBuilder()..update(updates)).build();

  _$Article._({this.title, this.url, this.by, this.time, this.score})
      : super._() {
    if (title == null) {
      throw new BuiltValueNullFieldError('Article', 'title');
    }
    if (url == null) {
      throw new BuiltValueNullFieldError('Article', 'url');
    }
    if (by == null) {
      throw new BuiltValueNullFieldError('Article', 'by');
    }
    if (time == null) {
      throw new BuiltValueNullFieldError('Article', 'time');
    }
    if (score == null) {
      throw new BuiltValueNullFieldError('Article', 'score');
    }
  }

  @override
  Article rebuild(void Function(ArticleBuilder) updates) =>
      (toBuilder()..update(updates)).build();

  @override
  ArticleBuilder toBuilder() => new ArticleBuilder()..replace(this);

  @override
  bool operator ==(Object other) {
    if (identical(other, this)) return true;
    return other is Article &&
        title == other.title &&
        url == other.url &&
        by == other.by &&
        time == other.time &&
        score == other.score;
  }

  @override
  int get hashCode {
    return $jf($jc(
        $jc($jc($jc($jc(0, title.hashCode), url.hashCode), by.hashCode),
            time.hashCode),
        score.hashCode));
  }

  @override
  String toString() {
    return (newBuiltValueToStringHelper('Article')
          ..add('title', title)
          ..add('url', url)
          ..add('by', by)
          ..add('time', time)
          ..add('score', score))
        .toString();
  }
}

class ArticleBuilder implements Builder<Article, ArticleBuilder> {
  _$Article _$v;

  String _title;
  String get title => _$this._title;
  set title(String title) => _$this._title = title;

  String _url;
  String get url => _$this._url;
  set url(String url) => _$this._url = url;

  String _by;
  String get by => _$this._by;
  set by(String by) => _$this._by = by;

  int _time;
  int get time => _$this._time;
  set time(int time) => _$this._time = time;

  int _score;
  int get score => _$this._score;
  set score(int score) => _$this._score = score;

  ArticleBuilder();

  ArticleBuilder get _$this {
    if (_$v != null) {
      _title = _$v.title;
      _url = _$v.url;
      _by = _$v.by;
      _time = _$v.time;
      _score = _$v.score;
      _$v = null;
    }
    return this;
  }

  @override
  void replace(Article other) {
    if (other == null) {
      throw new ArgumentError.notNull('other');
    }
    _$v = other as _$Article;
  }

  @override
  void update(void Function(ArticleBuilder) updates) {
    if (updates != null) updates(this);
  }

  @override
  _$Article build() {
    final _$result = _$v ??
        new _$Article._(
            title: title, url: url, by: by, time: time, score: score);
    replace(_$result);
    return _$result;
  }
}

// ignore_for_file: always_put_control_body_on_new_line,always_specify_types,annotate_overrides,avoid_annotating_with_dynamic,avoid_as,avoid_catches_without_on_clauses,avoid_returning_this,lines_longer_than_80_chars,omit_local_variable_types,prefer_expression_function_bodies,sort_constructors_first,test_types_in_equals,unnecessary_const,unnecessary_new
