#!/usr/bin/perl
#
# compare two groups of equal length (per row) binary data
# looking for similarities between each group, both groups,
# and differences between individual groups
#
# -samy kamkar

use strict;
use Term::ANSIColor;

my $verbose = $ARGV[0] eq "-v" ? shift() : 0;
my $noconv = $ARGV[0] eq "-n" ? shift() : 0;
die "usage: $0 [-v] [-n] [-h] <file>\n" if -t STDIN && !@ARGV;
my $hex = $ARGV[0] eq "-h" ? shift(@ARGV) : 0;

# binary set a and b
my (@a, @b, @orig);
my $next = 0;
my $ind = 0;
my @comments;

# read in our data
while (<>)
{
  chomp;
#  s/\s//g;

  # strip comment if present
  s/(\s*#.*)//;
  my $comment = $1;

  if ($_ eq "") { $next++; next; }
  else
  {
    push @orig, $_;
  }

  # already binary
  unless ($noconv)
  {
    if (/^[01\s_]+$/) { }
    elsif (/^[a-f\d\s_]+/i) # hex
    {
      s/([a-f\d])/unpack("B4", pack("H", $1))/ieg if !$hex;
    }
    else # ascii
    {
      s/(.)/unpack("B8", $1)/eg;
    }
  }
  my $bits = [split //];
  $next ? push(@b, $bits) : push(@a, $bits);
  push(@comments, $comment);
}

# bit length
my $bitlen = @{$a[0]};

# find common bits between pieces
my @common = find_common(@a, @b);
my @common_a = find_common(@a);
my @common_b = find_common(@b);

# find differences between the two groups
my @diff = map { !$common[$_] && $common_a[$_] && $common_b[$_] ? 1 : 0 } 0 .. $bitlen-1;

# now print the sets
cmpr(\@a, \@common_a);
midrow();
# print just same/diff rows easier
cmpr(\@b, \@common_b);

# print bits
printbits();

sub printbits
{
  my $max = ($bitlen - 1) % 8;
  print " " x (length($orig[0]) + 1) if $verbose;
  foreach (1 .. $bitlen)
  {
    print color($max == 0 ? 'bold' : $max == 4 ? 'yellow' : 'reset') . $max . color('reset');
    $max = ($max - 1) % 8;
  }
  print "\n";
}

sub midrow
{
  print " " x (length($orig[0]) + 1) if $verbose;
  for (my $i = 0; $i < $bitlen; $i++)
  {
    my $color =
      $diff[$i] ? 'bold blue' : # if different between groups
      $common[$i] ? 'bold green' : # same between groups
      $common_a[$i] || $common_b[$i] ? 'cyan' : # common in single group
      'reset';
    my $letter = $diff[$i] ? 'X' : $common[$i] ? '=' : $common_a[$i] ? '^' : $common_b[$i] ? 'v' : '-';
    print color($color) . $letter . color('reset');
  }
  print "\n";
}
sub cmpr
{
  my ($rows, $common) = @_;

  # go through rows of the set
  foreach my $bits (@{$rows})
  {
    print "$orig[$ind++] " if $verbose;
    # go through each bit in the row
    for (my $i = 0; $i < $bitlen; $i++)
    {
      my $bit = $bits->[$i];
      my $commbit = $common->[$i];
      my $color =
        $bit ne '0' && $bit ne '1' ? 'reset' : # ignore space/underlines
        $common[$i] ? 'green' : # same on all rows is green
        $diff[$i] ? ($bit ? 'magenta' : 'red') : # common in this set and not other is blue/red
        $commbit ? 'cyan' : # common just in the group
        'reset';
      print color($color) . $bit . color('reset');
    }
    print shift(@comments);
    print "\n";
  }
#  print "\n";
}

# find common bits among all rows
sub find_common
{
  my @common = (1) x $bitlen;
  my @lastbit = (-1) x $bitlen;
  # go through all array refs passed in
  foreach my $bits (@_)
  {
    # go through all bits in the array ref
    for (my $i = 0; $i < @{$bits}; $i++)
    {
      my $bit = $bits->[$i];
      # ignore comparing first bit (nothing to compare to yet)
      if ($lastbit[$i] != -1)
      {
        # if last bit is different
        if ($lastbit[$i] != $bit)
        {
          $common[$i] = 0;
        }
      }
      $lastbit[$i] = $bit;
    }
  }

  #print "@common\n";
  return @common;
}