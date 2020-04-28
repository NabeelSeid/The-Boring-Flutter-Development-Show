import 'package:flutter/material.dart';
import 'package:hackernews_flutter/src/json_parsing.dart';
import 'src/article.dart';
import 'package:http/http.dart' as http;
import 'package:url_launcher/url_launcher.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  List<int> _articles = [
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

  Future<Article> _getArticle(int id) async {
    final storyUrl = 'https://hacker-news.firebaseio.com/v0/item/${id}.json';
    final storyRes = await http.get(storyUrl);
    return parseArticle(storyRes.body);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: ListView(
        children: _articles
            .map((item) => FutureBuilder<Article>(
                future: _getArticle(item),
                builder: (_, AsyncSnapshot<Article> snapshot) {
                  if (snapshot.connectionState == ConnectionState.done) {
                    if (snapshot.hasData) {
                      return _buildItem(snapshot.data);
                    } else {
                      return Text('No Data');
                    }
                  } else {
                    return Center(
                      child: CircularProgressIndicator(),
                    );
                  }
                }))
            .toList(),
      ),
    );
  }

  Widget _buildItem(Article e) => Padding(
        key: Key(e.title),
        padding: const EdgeInsets.all(16.0),
        child: ExpansionTile(
          title: Text(e.title),
          children: <Widget>[
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: <Widget>[
                Text("${e.descendants} comments"),
                IconButton(
                    icon: Icon(Icons.launch),
                    onPressed: () async {
                      if (await canLaunch(e.url)) launch(e.url);
                    })
              ],
            )
          ],
        ),
      );
}
