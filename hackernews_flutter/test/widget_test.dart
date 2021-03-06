import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:hackernews_flutter/main.dart';

void main() {
  testWidgets('clicking tile opens it', (WidgetTester tester) async {
    await tester.pumpWidget(MyApp());

    expect(find.byIcon(Icons.launch), findsNothing);

    await tester.tap(find.byType(ExpansionTile).first);

    await tester.pump();

    expect(find.byIcon(Icons.launch), findsOneWidget);
  }, skip: true);
}
