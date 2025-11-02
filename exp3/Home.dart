import 'package:flutter/material.dart';
import 'package:pizza_app/screens/order.dart';
class Home extends StatelessWidget
{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return new Scaffold(
      appBar: new AppBar(title: new Text('Pizza Demo'),),
      body: new Center(
       child: new Container(
              padding: new EdgeInsets.all(32.0),
              child: new Column(
                children: <Widget>[
                  new Image.asset('images/pizza.png'),
                  new ElevatedButton(
                      child: new Text('Order'),
                      onPressed: () {Navigator.of(context).pushNamed('/Order');}
                  )
                ],
              ),
      ),
      )
    );
  }
}