import 'package:flutter/material.dart';
import 'package:hackernews_flutter/src/hn_bloc.dart';
import 'src/article.dart';
import 'package:url_launcher/url_launcher.dart';

void main() {
  HackerNewsBloc hnBloc = HackerNewsBloc();
  runApp(MyApp(bloc: hnBloc));
}

class MyApp extends StatelessWidget {
  final HackerNewsBloc bloc;

  MyApp({Key key, this.bloc}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page', bloc: bloc),
    );
  }
}

class MyHomePage extends StatefulWidget {
  final String title;
  final HackerNewsBloc bloc;

  MyHomePage({Key key, this.title, this.bloc}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: StreamBuilder<List<Article>>(
        stream: widget.bloc.articles,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return ListView(
              children:
                  snapshot.data.map((article) => _buildItem(article)).toList(),
            );
          } else if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else {
            return Text('No Data');
          }
        },
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
