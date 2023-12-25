#include <algorithm>
#include <ctime>
#include <iostream>
#include <queue>
#include <random>
#include <vector>
#define pii pair<int, int>
#define mp(x, y) make_pair(x, y)
#define f first
#define s second
using namespace std;
const int MAXN = 30;
int a, b, c;
vector<pair<pii, pii> > edge, nedge;
bool operator==(pii x, pii y) { return x.f == y.f && x.s == y.s; }
bool operator!=(pii x, pii y) { return (x.f != y.f) || (x.s != y.s); }
pii fa[MAXN + 10][MAXN + 10];
pii getfa(int x, int y)
{
	if (fa[x][y] == mp(x, y))
		return fa[x][y];
	return fa[x][y] = getfa(fa[x][y].f, fa[x][y].s);
}
int main()
{
	freopen("maze.out", "w", stdout);
	srand(unsigned(time(0)));
	a = rand() % MAXN + 1;
	b = rand() % MAXN + 1;
	pii srt, fin;
	if (a < b)
		swap(a, b);
	srt = mp(0, rand() % b);
	fin = mp(a - 1, rand() % b);
	while (fin.f == srt.f && fin.s == srt.s)
	{
		fin = mp(a - 1, rand() % b);
	}
	for (int i = 0; i < a; ++i)
	{
		for (int j = 0; j < b; ++j)
		{
			pii now = mp(i, j);
			fa[i][j] = mp(i, j);
			if (i - 1 >= 0)
			{
				pii element = mp(i - 1, j);
				edge.push_back(mp(now, element));
			}
			if (i + 1 < a)
			{
				pii element = mp(i + 1, j);
				edge.push_back(mp(now, element));
			}
			if (j - 1 >= 0)
			{
				pii element = mp(i, j - 1);
				edge.push_back(mp(now, element));
			}
			if (j + 1 < b)
			{
				pii element = mp(i, j + 1);
				edge.push_back(mp(now, element));
			}
		}
	}
	while (!edge.empty())
	{
		int value = rand() % edge.size();
		pair<pii, pii> now = edge[value];
		edge.erase(edge.begin() + value);
		pii fa1 = getfa(now.f.f, now.f.s), fa2 = getfa(now.s.f, now.s.s);
		if (fa1.f == fa2.f && fa1.s == fa2.s)
			continue;
		fa[fa1.f][fa1.s] = fa[fa2.f][fa2.s];
		nedge.push_back(now);
	}
	printf("%d %d\n%d\n", a, b, nedge.size());
	printf("%d %d %d %d\n", srt.f, srt.s, fin.f, fin.s);
	for (auto now : nedge)
	{
		printf("%d %d %d %d\n", now.f.f, now.f.s, now.s.f, now.s.s);
	}
	return 0;
}
