import 'package:flutter/material.dart';
import 'src/article.dart';
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
  List<Article> _articles = articles;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Builder(builder: (BuildContext context) {
        return RefreshIndicator(
          onRefresh: () async {
            await Future.delayed(const Duration(seconds: 1));
            setState(() {
              _articles.removeAt(0);
            });
            Scaffold.of(context).showSnackBar(SnackBar(
              content: Text("Removed: ${articles[0].text}"),
            ));
          },
          child: Center(
            child: ListView(
              children: _articles.map(_buildItem).toList(),
            ),
          ),
        );
      }),
    );
  }

  Widget _buildItem(Article e) => Padding(
        key: Key(e.text),
        padding: const EdgeInsets.all(16.0),
        child: ExpansionTile(
          title: Text(e.text),
          children: <Widget>[
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: <Widget>[
                Text("${e.commentsScore} comments"),
                IconButton(
                    icon: Icon(Icons.launch),
                    onPressed: () async {
                      if (await canLaunch(e.domain)) launch(e.domain);
                    })
              ],
            )
          ],
        ),
      );
}
